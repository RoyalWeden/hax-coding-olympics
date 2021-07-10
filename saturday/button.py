import pygame
import sys
import os

pygame.mixer.init()
pygame.init()
sound_path = 'saturday/sounds'

res = (720, 720)
screen = pygame.display.set_mode(res)

color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_black = (0, 0, 0)

dim = (screen.get_width(), screen.get_height()) # (width, height)

smallfont = pygame.font.SysFont('Corbel', 35)

easy_text = smallfont.render('Easy', True, color_black)

easy_sound = pygame.mixer.Sound(os.path.join(sound_path, 'that_was_easy.wav'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (dim[0]/2-120)<=mouse[0]<=(dim[0]/2+120) and (dim[1]/2-40)<=mouse[1]<=(dim[1]/2+40):
                pygame.mixer.Sound.stop(easy_sound)
                pygame.mixer.Sound.play(easy_sound)

    screen.fill(color_white)

    mouse = pygame.mouse.get_pos() # (x, y)

    pygame.draw.rect(screen, color_red, [dim[0]/2-120, dim[1]/2-40, 240, 80])

    screen.blit(easy_text, (dim[0]/2-35, dim[1]/2-20))

    pygame.display.update()