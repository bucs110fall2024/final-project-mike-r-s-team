from openai import OpenAI

class API:
    
    def __init__(self, api_key):
        self.client = OpenAI(api_key= api_key)
        self.client.files.create(
        file=open(r"template_final_project-master\src\ADHD_training_set.jsonl", "rb"),
        purpose="fine-tune"
        )
        self.messages = []
    
    def chist(self):
        history_file = open(r"template_final_project-master\src\chat_history.jsonl", 'r')
        self.chat_history = history_file.read()
        history_file.close()
    
    def save(self):
        history_file = open(r"template_final_project-master\src\chat_history.jsonl", 'a')
        history_file.append(self.messages)
        history_file.close()
    
    def uinp(self):
        self.user_input
    
    def prompt(self):
        self.completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a doctor-like bot that will use your knowledge of ADHD to help a patient who is communicating with you as best as you can."},
                {
                    "role": "user",
                    "content": "Did all 10 training prompts sucessfully go through?"
                }
            ]
        )
    def messret(self):
        return self.messages