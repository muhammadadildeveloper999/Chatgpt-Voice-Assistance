import streamlit as st
import openai
import azure.cognitiveservices.speech as speechsdk
import time
import pyaudio

openai.api_key = "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"

def generate_openai_response(question):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=250
    )
    return response.choices[0].text.strip()

def text_to_speech(text_to_speak):
    speech_config = speechsdk.SpeechConfig(subscription="694377aee2554690925844852c36c82e", region="westus")
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    synthesizer.speak_text_async(text_to_speak)

def speech_to_text():
    p = pyaudio.PyAudio()
    available_input_devices = []
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        if device_info['maxInputChannels'] > 0:
            available_input_devices.append(device_info['name'])

    if not available_input_devices:
        st.sidebar.error("No audio input devices found. Please connect a microphone or headphones.")
        return
    
    speech_config = speechsdk.SpeechConfig(subscription="694377aee2554690925844852c36c82e", region="westus")
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    st.sidebar.image("CBLogo.png", caption="Your Robot", use_column_width=True)
    st.sidebar.write("Press the 'Start Button' and ask me a question, and I will respond...")  # Instruction section
    start_button_pressed = st.sidebar.button("Start Program", key="start_button_key")

    
    
    if start_button_pressed:
        st.sidebar.write("Note:  You can start your question over by saying 'Stop' during question input...")  # Instruction section
        st.sidebar.write("You can end the chat session by saying 'Exit'")  # Instruction section

        while True:
            st.write("🎤 Start speaking...")
            start_time = time.time()  
            result = recognizer.recognize_once()

            elapsed_time = time.time() - start_time

            if elapsed_time >= 300:
                st.write("⏳ No speech detected for 5 minutes. Session timed out.")
                break

            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                user_question = result.text

                if "stop" in user_question.lower():
                    st.write("🔄 Restarting prompt...")
                    continue

                if "exit" in user_question.lower():
                    st.write("👋 Goodbye for now...")
                    break

                if user_question:
                    response_text = generate_openai_response(user_question)

                    st.markdown(f"<div style='background-color: #ADD8E6; padding: 10px; border-radius: 5px; text-align: left; color: black; margin-bottom: 10px;'>"
                                f"👤 You: {user_question}</div>",
                                unsafe_allow_html=True)
                    
                    st.markdown(f"<div style='background-color: #87CEFA; padding: 10px; border-radius: 5px; text-align: left; color: black; margin-bottom: 10px;'>"
                                f"🤖 Assistant: {response_text}</div>",
                                unsafe_allow_html=True)

                    # Speak the generated response using Azure Speech Services
                    text_to_speech(response_text)
            elif result.reason == speechsdk.ResultReason.NoMatch:
                st.write("")
            else:
                st.write("⚠️ Speech recognition failed. Please try again.")


# Main Streamlit app
if __name__ == "__main__":
    st.title("ChatGPT Speech Assistant")
    st.write("🤖 Welcome to the ChatGPT Speech Assistant powered by OpenAI and Azure Speech Studio.")
    
    main_column = st.beta_container()
    
    with main_column:
        # Display content in the main column
        st.write("Main content goes here.")
        
    # Call the speech_to_text function
    speech_to_text()
