# Conversational-Chatbot-with-Speech-to-Text-and-Text-to-Speech

This project is a conversational chatbot that converts speech to text, processes the input using the Llama3 Large Language Model (LLM), and outputs speech using Google Text-to-Speech (gTTS). The chatbot creates a seamless interaction experience, allowing users to engage with it through spoken language.

## Features

- **Speech-to-Text**: Uses `SpeechRecognition` to capture and convert user speech to text.
- **LLM Processing**: Processes text through the Llama3 model for generating intelligent and conversational responses.
- **Text-to-Speech**: Converts the response text to speech using `gTTS` for audible output.

## Technologies Used

- **SpeechRecognition**: The SpeechRecognition Python library provides easy-to-use tools for capturing and converting speech into text. It supports multiple speech recognition engines, including Google Web Speech API, and works with both online and offline modes. The library allows you to capture audio from microphones or audio files, making it versatile for a wide range of applications.

- **Llama3**: The new Llama 3 models with 8B and 70B parameters represent a significant advancement over Llama 2, setting a new benchmark for large language models at these scales. Enhanced pretraining and post-training have made both the pretrained and instruction-fine-tuned versions the most advanced models currently available at these parameter levels. Post-training improvements have led to reduced false refusal rates, better alignment, and more diverse responses. Additionally, Llama 3 demonstrates improved abilities in reasoning, code generation, and instruction following, making it more steerable.  
  [Learn more about Llama3](https://ollama.com/library/llama3)

- **gTTS**: Google Text-to-Speech, a Python library and CLI tool, interfaces with Google Translate’s text-to-speech API. It can write spoken MP3 data to a file, a file-like object (bytestring) for further audio manipulation, or stdout. It features flexible pre-processing and tokenizing.

## Setup and Installation

1. **Create a virtual environment**:

   - For Windows:
     ```bash
     python -m venv llama
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned Process
     .\llama3\Scripts\activate
     ```

   - For macOS:
     ```bash
     python3 -m venv llama3
     source llama3/bin/activate
     ```

2. **Install the required dependencies**:

   - For Windows:
     ```bash
     pip install -r .\requirements.txt
     ```

   - For macOS:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the application**:
   - Pull Llama3 from Ollama:
     ```bash
     ollama pull llama3
     ```
   - Run the script:
     ```bash
     python sr_llama3_gtts.py
     ```

## How It Works

1. The chatbot listens for live user speech and converts it to text using the `SpeechRecognition` library.
2. The text is sent to the Llama3 LLM to generate an appropriate response.
3. The response is then converted back to speech using `gTTS` and played for the user.
4. The conversation continues until the user says “exit”, which prompts the bot to stop.

## Requirements

- Download Ollama from [https://ollama.com/](https://ollama.com/)
- For Windows users, add the Ollama installation to `Path` in the System Environment Variables.

- **Python** 3.8+
- Libraries:
  - `SpeechRecognition`
  - `gTTS`
  - `PyAudio`
  - `pydub`
  - `ffmpeg`
  - `ollama`

## Usage

Simply run the `.py` file and start speaking! The chatbot will respond to your speech with intelligent and engaging replies. To exit the conversation, say "exit".

## Results

https://github.com/user-attachments/assets/7a814434-117e-40b7-bc2a-827f76169c02

