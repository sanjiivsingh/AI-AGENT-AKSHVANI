from openai import OpenAI
from dotenv import load_dotenv
import os

#Load Configuration from .env
load_dotenv()

# Create AI Client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("=" * 40)
print("                Akshvani")
print("=" * 40)

while True:
    user_input = input("\n You : ")

    if user_input.lower() == "quit" :
        print("\nAkshvani : Goodbye!")
        break
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    print("\nAkshvani :", response.choices[0].message.content)
