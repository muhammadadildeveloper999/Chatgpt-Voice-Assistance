# ChatGPT Speech Assistant

This application is a ChatGPT Speech Assistant powered by OpenAI and Azure Speech Studio, providing speech-to-text and text-to-speech functionalities.

## Features

- **Voice Interaction**: Users can speak questions, and the application utilizes Azure Speech Studio for speech recognition.
- **OpenAI Integration**: The app generates responses to user queries using OpenAI's powerful text generation capabilities.
- **Real-time Conversation**: Conducts a seamless conversation between the user and the AI assistant.
- **Interactive Interface**: Utilizes Streamlit for a user-friendly interface.

## How to Use

1. **Installation**:
   - Install the required libraries by running: `pip install streamlit openai azure-cognitiveservices-speech pyaudio`.

2. **Run the Application**:
   - Run the application using Streamlit: `streamlit run app.py`.

3. **Usage**:
   - Click the 'Start Program' button on the sidebar to initiate the conversation.
   - Ask questions by speaking into your microphone.
   - Say 'Stop' to restart a question and 'Exit' to end the chat session.

## Requirements

- Python 3.6 or higher
- Streamlit
- OpenAI
- Azure Cognitive Services Speech SDK
- PyAudio

## Configuration

- **OpenAI API Key**: Replace `"OPENAI-KEY"` with your OpenAI API key in the `app.py` file.
- **Azure Subscription Key**: Replace `"AZURE-SPEECH-KEY"` with your Azure subscription key in the `app.py` file.

## Notes

- If no audio input devices are found, connect a microphone or headphones to use the speech recognition feature.
- The application times out after 5 minutes of no speech input.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, report issues, or suggest improvements!
