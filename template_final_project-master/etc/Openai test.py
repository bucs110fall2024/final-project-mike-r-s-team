from openai import OpenAI
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key= OPENAI_API_KEY)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a doctor-like bot that will use your knowledge of ADHD to help a patient who is communicating with you as best as you can."},
        {
            "role": "user",
            "content": "What are 3 symptoms of ADHD. Output your response without any markdown language."
        }
    ]
)
# messanges = [
#     {"role" : "system", "content" : "You are a doctor-like bot that will use your knowledge of ADHD to help a patient who is communicating with you as best as you can."}
# ]
# while True:
#     messange = input('User: ')
#     if messange:
#         completion = client.chat.completions.create(
#             model='gpt-4o-mini',
#             messanges.append({"role" : "user", "content" : messange}),
        # )
print(completion.choices[0].message)