import pygame
import pygame_menu
from src.sprites import Sprites
from src.chatbot import API

class Controller:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.background = pygame.image.load(r"template_final_project-master\assets\CS110_Background.png")
        self.background = pygame.transform.scale(self.background, (1280, 720))
        self.clipboard = pygame.image.load(r"template_final_project-master\assets\CS110_ClipBoard.png")
        self.clipboard = pygame.transform.scale(self.clipboard, (573, 587))
        
        pygame.init()
    
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        self.state = 'START'
    
    def mainloop(self):
        while True:
            if self.state == 'START':
                self.startloop()
            elif self.state == 'CHAT':
                self.chatloop()
            elif self.state == 'END':
                self.endloop()
    
    def startloop(self):
        self.menu = pygame_menu.Menu('Start Screen', self.width/2, self.height/2)
        self.menu.add.label('Click to start program', font_size= 28)
        self.menu.add.button(
            'Start', self.startchat, align=pygame_menu.locals.ALIGN_CENTER
        )
        
        while self.state == 'START':
            self.menu.update(pygame.event.get())
            self.menu.draw(self.screen)
            pygame.display.flip()
    
    def startchat(self):
        self.state = 'CHAT'
    
    def chatloop(self):
        self.API = API()
        xtextcor = 673
        ytextcor = 800
        while self.state == "CHAT":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 'END'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_esc:
                        self.state = "END"
                      
        messages = self.API.messret()
        y_offset = 0
        for text in messages:
            
        
    

        # update all sprite data
        #   self.sprites.update()

        # redraw the screen
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.clipboard, (673, 66))
        #   self.sprites.draw(self.screen)

        pygame.display.flip()
    
    def endloop(self):
        pass