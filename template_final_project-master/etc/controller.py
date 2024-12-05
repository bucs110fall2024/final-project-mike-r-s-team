from openai import OpenAI
import pygame
import pygame_menu
from gtts import gTTS
from src.pygui import GUI
from src.chatbot import API

class Controller:
    
    def __init__(self):
        
        pygame.init()
    
        self.state = 'START'
        
        self.loop = GUI()
        
        self.api = API()
    
    def mainloop(self):
        while True:
            if self.state == 'START':
                self.startloop()
            elif self.state == 'CHAT':
                self.chatloop()
            # elif self.state == 'END':
            #     self.endloop()
    
    def startloop(self):
        self.loop.start
        self.state = 'CHAT'
    
    def chatloop(self):
        ## This is the mainloop, so once we exit we cannot return without rerunning
        ## we have to get the api key from pygui before we can run self.api.chat()
        init = 1
        while init > 0:
            self.api.chat()