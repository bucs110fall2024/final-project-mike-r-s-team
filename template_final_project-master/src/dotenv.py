import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
class Dotenv:
    
    def __init__(self):
        self.dotenv_path = find_dotenv()
    
    def loadgetkey(self, path):
        load_dotenv(self.dotenv_path)
        return os.getenv("OPENAI_API_KEY")