from openai import OpenAI

class API:
    
    def __init__(self):
        self.messages = None
    
    def chat(self, messages, api_key, context = "You are a doctor like chatbot who's purpose is to help people with ADHD", message_flipper = 'stay'):
        self.client = OpenAI(api_key= api_key)
        self.client.files.create(
        file=open("template_final_project-master\src\ADHD_training_set.jsonl", "rb"),
        purpose= "fine-tune"
        )
        
        if message_flipper == 'innit':
            self.messages.append({"role" : "system", "content" : context})
        
        ## Get input here labeled user_input
        ## Add this input to messages
        
        completion = self.client.chat.completions.create(
            model= 'gpt-4o-mini',
            messages= messages
        )
                
        messages.append(
                {"role" : "assistant", "content" : completion.choices[0].message.content}
            )
        
        return messages