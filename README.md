# Gemini Multi-Turn Chat

A simple context-aware chatbot using the Google Gemini Free API. This console application maintains conversation history across multiple turns, allowing the AI to "remember" previous parts of the conversation.

## Features

- **Multi-turn conversations** with context preservation
- **Configurable model parameters** (temperature, top-p, max tokens)
- **Console-based interface** - no GUI required
- **Extensible conversation flow** - continue chatting as long as you want
- **Error handling** for API issues and missing dependencies

## What the Script Does

1. **Initializes** a Gemini chat session using the `gemini-1.5-flash` model
2. **Prompts** the user for model configuration (temperature, top-p, max tokens)
3. **Collects** user input for the first message and sends it to Gemini
4. **Maintains context** by using Gemini's chat session functionality
5. **Prompts** for a second message and sends it with full conversation history
6. **Optionally continues** the conversation for additional turns
7. **Prints** the final Gemini response to the console

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- A Google Gemini API key (free from [Google AI Studio](https://aistudio.google.com/))

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gemini-multi-turn-chat.git
   cd gemini-multi-turn-chat
   ```

2. **Install required dependencies:**
   ```bash
   pip install google-generativeai
   ```

3. **Set up your API key** (choose one method):
   
   **Method 1: Environment Variable (Recommended)**
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```
   
   **Method 2: Enter when prompted**
   - The script will ask for your API key if not found in environment variables

## How to Run

1. **Navigate to the project directory:**
   ```bash
   cd gemini-multi-turn-chat
   ```

2. **Run the script:**
   ```bash
   python3 gemini_chat.py
   ```

3. **Follow the prompts:**
   - Configure model parameters (or press Enter for defaults)
   - Enter your first message
   - Enter a follow-up message
   - Optionally continue the conversation
   - The final response will be printed at the end

## Example Usage

```
=== Context-Aware Gemini Chatbot ===
This chatbot maintains conversation context across multiple turns.

--- Model Configuration (Optional) ---
Press Enter to use defaults, or specify custom values:
Temperature (0.0-2.0, default 0.7): 0.9
Top-p (0.0-1.0, default 0.95): 
Max output tokens (default 1024): 

Using configuration: {'temperature': 0.9, 'top_p': 0.95, 'max_output_tokens': 1024}

=== Starting Conversation ===

--- Turn 1 ---
Enter your first message: Tell me about Python programming

Sending to Gemini...

Gemini: Python is a high-level, interpreted programming language...

--- Turn 2 ---
Enter your follow-up message: What are its main advantages?

Sending to Gemini (with context)...

Gemini: Based on what I mentioned about Python, its main advantages include...

--- Turn 3 (Optional) ---
Continue conversation? (y/n, default n): n

=== Final Response ===
Based on what I mentioned about Python, its main advantages include...
```

## Model Parameters

The script allows you to configure:

- **Temperature (0.0-2.0)**: Controls randomness/creativity
  - Lower values (0.1-0.4): More focused, deterministic responses
  - Higher values (0.8-1.5): More creative, varied responses
  
- **Top-p (0.0-1.0)**: Controls diversity via nucleus sampling
  - Lower values: More focused on high-probability words
  - Higher values: Considers more word options
  
- **Max Output Tokens**: Limits response length (1-8192)

## Dependencies

- `google-generativeai`: Official Google Gemini API client

## Security Notes

- **Never commit your API key** to version control
- Use environment variables or secure credential management
- The provided `.gitignore` excludes common sensitive files

## Troubleshooting

**Import Error:**
```
pip install google-generativeai
```

**API Key Issues:**
- Ensure your API key is valid and has Gemini API access
- Check that environment variables are set correctly

**Network Issues:**
- Verify internet connection
- Check if corporate firewalls are blocking the API

## License

This project is open source and available under the MIT License.
