import os
import openai
import sys
import warnings
warnings.filterwarnings('ignore') # setting ignore as a parameter
warnings.filterwarnings(action='ignore', category=FutureWarning)

openai.api_type = "azure"
openai.api_base =  os.getenv("OPENAI_API_ENDPOINT")
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_completion(message_text):
    completion = openai.ChatCompletion.create(
        engine="GPT35Turbo",
        messages=message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return completion

def main():
    # Check if message_text is provided as a command line argument
    if len(sys.argv) < 2:
        print("Usage: python script.py 'message_text'")
        sys.exit(1)

    # Get message_text from command line argument
    message_text = [{"role":"system","content":"You are an AI assistant that helps people find information."}]
    user_message = {"role": "user", "content": sys.argv[1]}
    message_text.append(user_message)

    # Generate completion
    completion = generate_completion(message_text)

    # Extract and print the message content
    if 'choices' in completion and len(completion['choices']) > 0:
        message_content = completion['choices'][0]['message']['content']
        print("Generated Message Content:")
        print(message_content)
    else:
        print("No message content found in the response.")

if __name__ == "__main__":
    main()