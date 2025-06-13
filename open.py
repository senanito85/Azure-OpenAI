import os
import sys
import warnings
from openai import AzureOpenAI

warnings.filterwarnings('ignore', category=FutureWarning)

# Check environment variables
endpoint = os.getenv("OPENAI_API_ENDPOINT")
api_key = os.getenv("OPENAI_API_KEY")
if not endpoint or not api_key:
    print("Error: OPENAI_API_ENDPOINT and OPENAI_API_KEY must be set in environment variables.")
    sys.exit(1)

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_version="2024-12-01-preview",
    api_key=api_key
)

def generate_completion(message_text):
    try:
        completion = client.chat.completions.create(
            model="stellars-chatbot",
            messages=message_text,
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0
        )
        return completion
    except Exception as e:
        print(f"Error generating completion: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python open.py 'your message here'")
        sys.exit(1)

    message_text = [
        {"role": "system", "content": "You are an AI assistant that helps people find information."},
        {"role": "user", "content": sys.argv[1]}
    ]

    completion = generate_completion(message_text)

    if completion and hasattr(completion, 'choices') and len(completion.choices) > 0:
        message_content = completion.choices[0].message.content
        print("Generated Message Content:")
        print(message_content)
    else:
        print("No message content found in the response.")

if __name__ == "__main__":
    main()