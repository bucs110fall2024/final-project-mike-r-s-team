from gtts import gTTS
import pygame

mytext = 'Welcome Users!'

language = 'en'

myobj = gTTS(text = mytext, lang = language, slow = False)

myobj.save('welcome.ogg')

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('welcome.ogg')
sound.play()
while pygame.mixer.get_busy():
    pygame.time.delay(100)