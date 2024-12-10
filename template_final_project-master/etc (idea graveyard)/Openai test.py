from openai import OpenAI
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key= OPENAI_API_KEY)
client.files.create(
  file=open("template_final_project-master\src\ADHD_training_set.jsonl", "rb"),
  purpose="fine-tune"
)
messagess = []
assistant_context = input('What would you like the computer to know about itself: ')
messagess.append(
    {"role" : "system", "content" : assistant_context}
)
while True:
    messagess.append(
        {"role" : "user", "content" : input('What is your question: ')}
    )
    completion = client.chat.completions.create(
        model= 'gpt-4o-mini',
        messages= messagess
    )
    print(completion.choices[0].message.content)
    messagess.append(
        {"role" : "assistant", "content" : completion.choices[0].message.content}
    )
    yene = input('Yes or No: ')
    if yene == 'No':
        break
print(messagess)