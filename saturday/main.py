import pygame
import sys
import os
from pygame_objects import PGObject, PGMouse, PGButton, PGText
import time
import random

pygame.mixer.init()
pygame.init()
sound_path = 'saturday/sounds'

res = (900, 600)
screen = pygame.display.set_mode(res)

color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_black = (0, 0, 0)

dim = (screen.get_width(), screen.get_height()) # (width, height)

smallfont = pygame.font.SysFont('Corbel', 35)

easy_sound = pygame.mixer.Sound(os.path.join(sound_path, 'that_was_easy.wav'))

def play_easy_sound():
    pygame.mixer.Sound.stop(easy_sound)
    pygame.mixer.Sound.play(easy_sound)
    print('Played: That was easy')

main_mouse = PGMouse()
easy_button = PGButton(
    screen,
    main_mouse,
    color_red,
    (dim[0]/2, dim[1]/2),
    (240, 80),
    play_easy_sound
)
easy_text = PGText(
    screen,
    smallfont,
    'Easy',
    color_black,
    loc_obj=easy_button
)

dir = (random.choice([-1,1]), random.choice([-1,1]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            easy_button.on_click()

    screen.fill(color_white)
    
    easy_button.render()
    easy_text.render()

    easy_button.move(dir)
    time.sleep(.01)
    dir = easy_button.in_bounds_dir(dir)

    pygame.display.update()