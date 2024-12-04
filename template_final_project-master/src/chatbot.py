from openai import OpenAI

class API:
    
    def __init__(self, api_key):
        client = OpenAI(api_key= api_key)
        client.files.create(
        file=open(r"template_final_project-master\src\ADHD_training_set.jsonl", "rb"),
        purpose="fine-tune"
        )
        
        self.messages = []
        self.chat_history = None
        self.completion = None
    
    def chist(self):
        history_file = open(r"template_final_project-master\src\chat_history.jsonl", 'r')
        self.chat_history = history_file.read()
        history_file.close()
    
    def save(self, messages):
        history_file = open(r"template_final_project-master\src\chat_history.jsonl", 'a')
        history_file.append(messages)
        history_file.close()
    
    def uinp(self):
        pass