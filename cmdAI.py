import os
import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Set your OpenAI API key here (replace 'your_openai_api_key_here' with your actual API key)
API_KEY = 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

# Define the API endpoint
API_URL = "https://api.openai.com/v1/engines/text-davinci-003/completions"

def query_ai(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "prompt": prompt,
        "max_tokens": 150  # Limit the response length
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()["choices"][0]["text"].strip()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error: {e}")
        return None

if __name__ == "__main__":
    print(f"{Fore.CYAN}Welcome to the AI Chatbot! Type 'exit' or 'quit' to end the conversation.")
    
    while True:
        # User input in green
        user_input = input(f"{Fore.GREEN}You: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print(f"{Fore.YELLOW}Goodbye!")
            break
        
        # AI response in blue
        ai_response = query_ai(user_input)
        if ai_response:
            print(f"{Fore.BLUE}AI: {ai_response}")