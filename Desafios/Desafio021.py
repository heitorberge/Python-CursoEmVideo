import pygame

pygame.init()
pygame.mixer.music.load("enzoyuki-enzo-yuki-porta-aberta-3fc9e614.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)