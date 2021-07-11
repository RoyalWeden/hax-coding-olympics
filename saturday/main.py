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
    new_btn = PGButton(
        screen,
        main_mouse,
        color_red,
        (dim[0]/2, dim[1]/2),
        (240, 80),
        play_easy_sound
    )
    new_txt = PGText(
        screen,
        smallfont,
        'Easy',
        color_black,
        loc_obj=new_btn
    )
    new_dir = (random.choice([-1,1]), random.choice([-1,1]))
    new_speed = random.random()*10+.1
    while new_dir == easy_button_dirs[0]:
        new_dir = (random.choice([-1,1]), random.choice([-1,1]))
    easy_buttons.append(new_btn)
    easy_texts.append(new_txt)
    easy_button_dirs.append(new_dir)
    easy_button_speeds.append(new_speed)

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
speed = random.random()*10+.1

easy_buttons = []
easy_texts = []
easy_button_dirs = []
easy_button_speeds = []
easy_buttons.append(easy_button)
easy_texts.append(easy_text)
easy_button_dirs.append(dir)
easy_button_speeds.append(speed)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(easy_buttons)):
                easy_buttons[i].on_click()

    screen.fill(color_white)
    
    for i in range(len(easy_buttons)):
        easy_buttons[i].render()
        easy_texts[i].render()

        easy_buttons[i].move(easy_button_dirs[i], easy_button_speeds[i])
        easy_button_dirs[i] = easy_buttons[i].in_bounds_dir(easy_button_dirs[i])

    time.sleep(.01)

    pygame.display.update()