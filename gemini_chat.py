#!/usr/bin/env python3
"""
Context-Aware Gemini Chat
A simple interactive chatbot using Google Gemini API with conversation context preservation.
"""

import os
from dotenv import load_dotenv
import sys
try:
    import google.generativeai as genai
except ImportError:
    print("Error: google-generativeai package not found.")
    print("Please install it with: pip install google-generativeai")
    sys.exit(1)

# Load environment variables
load_dotenv()

def get_api_key():
    """Get API key from environment variable or user input."""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("Gemini API key not found in environment variables.")
        print("Looking for .env file...")
        api_key = os.getenv('GEMINI_API_KEY')  # Try loading again after .env is loaded
        if not api_key:
            print("API key not found in .env file. Please enter your Gemini API key:")
            api_key = input().strip()
            if not api_key:
                print("API key is required to continue.")
                sys.exit(1)
    return api_key


def get_model_config():
    """Allow user to optionally configure model parameters."""
    print("\n--- Model Configuration (Optional) ---")
    print("Press Enter to use defaults, or specify custom values:")
    
    # Temperature configuration
    temp_input = input("Temperature (0.0-2.0, default 0.7): ").strip()
    try:
        temperature = float(temp_input) if temp_input else 0.7
        temperature = max(0.0, min(2.0, temperature))  # Clamp between 0-2
    except ValueError:
        temperature = 0.7
    
    # Top-p configuration
    top_p_input = input("Top-p (0.0-1.0, default 0.95): ").strip()
    try:
        top_p = float(top_p_input) if top_p_input else 0.95
        top_p = max(0.0, min(1.0, top_p))  # Clamp between 0-1
    except ValueError:
        top_p = 0.95
    
    # Max output tokens
    max_tokens_input = input("Max output tokens (default 1024): ").strip()
    try:
        max_tokens = int(max_tokens_input) if max_tokens_input else 1024
        max_tokens = max(1, min(8192, max_tokens))  # Reasonable limits
    except ValueError:
        max_tokens = 1024
    
    config = {
        'temperature': temperature,
        'top_p': top_p,
        'max_output_tokens': max_tokens
    }
    
    print(f"\nUsing configuration: {config}")
    return config


def main():
    """Main chatbot function."""
    print("=== Context-Aware Gemini Chatbot ===")
    print("This chatbot maintains conversation context across multiple turns.\n")
    
    # Get API key and configure
    api_key = get_api_key()
    genai.configure(api_key=api_key)
    
    # Get model configuration
    model_config = get_model_config()
    
    try:
        # Initialize the model with configuration
        generation_config = genai.types.GenerationConfig(
            temperature=model_config['temperature'],
            top_p=model_config['top_p'],
            max_output_tokens=model_config['max_output_tokens']
        )
        
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            generation_config=generation_config
        )
        
        # Start a chat session to maintain context
        chat = model.start_chat(history=[])
        
        print("\n=== Starting Conversation ===")
        
        # First turn
        print("\n--- Turn 1 ---")
        user_input_1 = input("Enter your first message: ").strip()
        if not user_input_1:
            print("No input provided. Exiting.")
            return
        
        print("\nSending to Gemini...")
        response_1 = chat.send_message(user_input_1)
        print(f"\nGemini: {response_1.text}")
        
        # Second turn (with context)
        print("\n--- Turn 2 ---")
        user_input_2 = input("Enter your follow-up message: ").strip()
        if not user_input_2:
            print("No input provided. Ending conversation.")
            print(f"\nFinal response: {response_1.text}")
            return
        
        print("\nSending to Gemini (with context)...")
        response_2 = chat.send_message(user_input_2)
        print(f"\nGemini: {response_2.text}")
        
        # Optional third turn and beyond
        turn_count = 3
        while True:
            print(f"\n--- Turn {turn_count} (Optional) ---")
            continue_chat = input("Continue conversation? (y/n, default n): ").strip().lower()
            
            if continue_chat not in ['y', 'yes']:
                break
            
            user_input = input("Enter your message: ").strip()
            if not user_input:
                print("No input provided. Ending conversation.")
                break
            
            print("\nSending to Gemini (with full context)...")
            response = chat.send_message(user_input)
            print(f"\nGemini: {response.text}")
            response_2 = response  # Update final response
            turn_count += 1
        
        # Print final response as required
        print(f"\n=== Final Response ===")
        print(response_2.text)
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Please check your API key and internet connection.")
        sys.exit(1)


if __name__ == "__main__":
    main()