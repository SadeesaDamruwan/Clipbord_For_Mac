import os
import pyperclip
import keyboard
import openai
from dotenv import load_dotenv

# Load the OpenAI API key from the .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize a variable to store the last content of the clipboard
last_clipboard_content = ""

def fetch_gpt_response(prompt):
    """Sends the clipboard content to the GPT-4 model for processing."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the appropriate GPT-4 model
            prompt=prompt,
            max_tokens=100  # Adjust the token limit as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None

def monitor_clipboard():
    """Monitors the clipboard and processes new content."""
    global last_clipboard_content

    while True:
        # Check if Command+B (⌘+B) is pressed to terminate the script
        if keyboard.is_pressed('cmd+b'):
            print("Terminating script...")
            break

        # Check if Command+X (⌘+X) is pressed to process the clipboard content
        if keyboard.is_pressed('cmd+x'):
            current_clipboard_content = pyperclip.paste()

            # Only process if the clipboard content has changed
            if current_clipboard_content != last_clipboard_content:
                print("New content detected, processing...")
                response = fetch_gpt_response(current_clipboard_content)

                if response:
                    pyperclip.copy(response)
                    print("Response copied to clipboard.")

                last_clipboard_content = current_clipboard_content

if __name__ == "__main__":
    print("Monitoring clipboard... Press ⌘+X to process, ⌘+B to terminate.")
    monitor_clipboard()
