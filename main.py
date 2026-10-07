from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    token=HF_TOKEN,
    provider="featherless-ai"
)

topic = input("Enter topic: ")
count = int(input("How many flashcards: "))

response = client.chat.completions.create(
    model="google/gemma-2-2b-it",
    messages=[
        {
            "role": "user",
            "content": f"""
Create {count} flashcards about {topic}.

Format:
Q: question
A: answer

Keep the answers short and easy to understand.
"""
        }
    ],
    max_tokens=500
)

print(response.choices[0].message.content)