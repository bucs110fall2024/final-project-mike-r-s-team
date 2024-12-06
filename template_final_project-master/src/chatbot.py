from openai import OpenAI

class Api:
    
    def __init__(self, api_key):
        
        self.client = OpenAI(api_key= api_key)
        self.client.files.create(
        file=open(r"template_final_project-master\src\ADHD_training_set.jsonl", "rb"),
        purpose= "fine-tune"
        )
    
    def chat(self, gpt_model, messages):
        '''
        takes in a list of dictionaries, which are lines from conversation, and returns the openai api's response as a part of the list
        args:       gpt_model   (str)   tells the api which ai model to use to respond to the user
                    messages    (list)  a list of dictionaries which are the lines of conversation between user and api
        return:     messages    (list)  a list of dictionaries which are the lines of conversation between user and api
        '''
        
        completion = self.client.chat.completions.create(
            model= gpt_model,
            messages= messages
        )
                
        messages.append(
                {"role" : "assistant", "content" : completion.choices[0].message.content}
            )
        
        return messages