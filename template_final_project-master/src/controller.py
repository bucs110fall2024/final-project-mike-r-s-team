import pygame_menu
import pygame
from src.player import Player
from src.background import Background
import tkinter


class Controller:
  
  def __init__(self):
    size = tkinter.Tk()
    self.height = size.winfo_screenheight()
    self.width = size.winfo_screenwidth()
    size.destroy()
    
    pygame.init()
    
    self.screen = pygame.display.set_mode(self.width, self.height)
    self.player = Player()
    self.sprites = pygame.sprite.Group((self.player))
    
    self.state = 'START'
    
  def mainloop(self):
    while True:
      if self.state == "GAME":
          self.gameloop()
      elif self.state == "END":
          self.endloop()
      elif self.state == "START":
          self.startloop()
    
  def startgame(self):
        self.state = "GAME"

  def startloop(self):
      self.menu = pygame_menu.Menu("Start Screen", self.width / 2, self.height / 2)
      self.menu.add.label("Click to start program", font_size=28)
      self.menu.add.button(
          "Start", self.startgame, align=pygame_menu.locals.ALIGN_CENTER
      )

      while self.state == "START":
          self.menu.update(pygame.event.get())
          self.menu.draw(self.screen)
          pygame.display.flip()

  def gameloop(self):
      while self.state == "GAME":
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  exit()
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_esc:
                      self.state = "END"

          # update all sprite data
          self.sprites.update()

          # redraw the screen
          self.screen.fill("purple")
          self.sprites.draw(self.screen)

          pygame.display.flip()
    
  def endloop(self):
      font_obj = pygame.font.SysFont(None, 48)
      msg = font_obj.render("Hope you enjoyed the game!", True, "black")

      while self.state == "END":
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  exit()
          self.screen.blit(msg, (50, 50))
          pygame.display.flip()