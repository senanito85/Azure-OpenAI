#Note: The openai-python library support for Azure OpenAI is in preview.
#Note: This code sample requires OpenAI Python library version 0.28.1 or lower.
import os
from openai import AzureOpenAI

client = AzureOpenAI(azure_endpoint="https://mehdi-ai.openai.azure.com/",
api_version="2023-07-01-preview",
api_key=os.getenv("OPENAI_API_KEY"))
import warnings
warnings.filterwarnings("ignore")


message_text = [{"role":"system","content":"Can you help me to write some code?"}]

completion = client.chat.completions.create(model="GPT35Turbo",
messages = message_text,
temperature=0.7,
max_tokens=800,
top_p=0.95,
frequency_penalty=0,
presence_penalty=0,
stop=None)

# Print the response
# print("Response:")
# print(completion)

# Extract and print the message content
if 'choices' in completion and len(completion.choices) > 0:
    message_content = completion.choices[0].message.content
    print("Generated Message Content:")
    print(message_content)
else:
    print("No message content found in the response.")