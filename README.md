# # Gemini Multi-Turn Chatbot

A simple interactive chatbot using Google's Gemini API that maintains conversation context across multiple turns.

## Features

- Multi-turn conversation with context preservation
- Simple console-based interface
- Configurable model parameters
- Error handling and user-friendly prompts

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Get a Gemini API key from Google Cloud Console:
   - Go to https://makersuite.google.com/app/apikey
   - Create a new API key
   - Set it as an environment variable or enter it when prompted

## Usage

1. Run the script:
```bash
python gemini_chat.py
```

2. Start chatting! The bot will:
   - Preserve conversation context across turns
   - Allow you to exit by typing 'exit'
   - Handle errors gracefully

## Security Note

Never commit your API key to version control. Always use environment variables or secure storage for API keys.
