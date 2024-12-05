import pygame
import pygame_menu

class GUI:
    
    def __init__(self):
        pygame.init()
        pygame.event.pump()

        self.width = 1280
        self.height = 720
        
        self.screen = pygame.display.set_mode((self.width, self.height))
    
    def start(self):
        running = True
        while running:
            self.menu = pygame_menu.Menu('Start Screen', self.width/2, self.height/2)
            self.menu.add.label('Click to start program', font_size= 28)
            self.menu.add.button( 
                'Start', running = False, align=pygame_menu.locals.ALIGN_CENTER
            )
            self.menu.update(pygame.event.get())
            self.menu.draw(self.screen)
            pygame.display.flip()