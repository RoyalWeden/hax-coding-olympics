import pygame
import sys
from src.gameobject import Button, GameObject, TextBox
from src.calculator import Calculator

pygame.mixer.init()
pygame.init()

res = (900, 600)
screen = pygame.display.set_mode(res)

color_white = (255, 255, 255)
color_black = (0, 0, 0)

calculator = Calculator()

smallfont = pygame.font.SysFont('Corbel', 35)

mouse = pygame.mouse

btn_one = Button(
    screen,
    (res[0]/2-110, res[1]/2-110),
    color_black,
    (100, 100),
    '1',
    smallfont,
    color_white,
    lambda: calculator.enter(1)
)
btn_two = Button(
    screen,
    (res[0]/2, res[1]/2-110),
    color_black,
    (100, 100),
    '2',
    smallfont,
    color_white,
    lambda: calculator.enter(2)
)
btn_three = Button(
    screen,
    (res[0]/2+110, res[1]/2-110),
    color_black,
    (100, 100),
    '3',
    smallfont,
    color_white,
    lambda: calculator.enter(3)
)
btn_four = Button(
    screen,
    (res[0]/2-110, res[1]/2),
    color_black,
    (100, 100),
    '4',
    smallfont,
    color_white,
    lambda: calculator.enter(4)
)
btn_five = Button(
    screen,
    (res[0]/2, res[1]/2),
    color_black,
    (100, 100),
    '5',
    smallfont,
    color_white,
    lambda: calculator.enter(5)
)
btn_six = Button(
    screen,
    (res[0]/2+110, res[1]/2),
    color_black,
    (100, 100),
    '6',
    smallfont,
    color_white,
    lambda: calculator.enter(6)
)
btn_seven = Button(
    screen,
    (res[0]/2-110, res[1]/2+110),
    color_black,
    (100, 100),
    '7',
    smallfont,
    color_white,
    lambda: calculator.enter(7)
)
btn_eight = Button(
    screen,
    (res[0]/2, res[1]/2+110),
    color_black,
    (100, 100),
    '8',
    smallfont,
    color_white,
    lambda: calculator.enter(8)
)
btn_nine = Button(
    screen,
    (res[0]/2+110, res[1]/2+110),
    color_black,
    (100, 100),
    '9',
    smallfont,
    color_white,
    lambda: calculator.enter(9)
)
btn_zero = Button(
    screen,
    (res[0]/2, res[1]/2+220),
    color_black,
    (100, 100),
    '0',
    smallfont,
    color_white,
    lambda: calculator.enter(0)
)

btn_plus = Button(
    screen,
    (res[0]/2-400, res[1]/2-175),
    color_black,
    (50, 50),
    '+',
    smallfont,
    color_white,
    lambda: calculator.enter('+')
)
btn_minus = Button(
    screen,
    (res[0]/2-345, res[1]/2-175),
    color_black,
    (50, 50),
    '-',
    smallfont,
    color_white,
    lambda: calculator.enter('-')
)
btn_times = Button(
    screen,
    (res[0]/2-290, res[1]/2-175),
    color_black,
    (50, 50),
    'x',
    smallfont,
    color_white,
    lambda: calculator.enter('*')
)
btn_divide = Button(
    screen,
    (res[0]/2-235, res[1]/2-175),
    color_black,
    (50, 50),
    '÷',
    smallfont,
    color_white,
    lambda: calculator.enter('/')
)
btn_power = Button(
    screen,
    (res[0]/2-400, res[1]/2-120),
    color_black,
    (50, 50),
    '^',
    smallfont,
    color_white,
    lambda: calculator.enter('^')
)

btn_equal = Button(
    screen,
    (res[0]/2+275, res[1]/2),
    color_black,
    (50, 50),
    '=',
    smallfont,
    color_white,
    lambda: calculator.calculate()
)

text_answer = TextBox(
    screen,
    (res[0]/2, res[1]/2-250),
    '0',
    smallfont,
    color_black
)

gameobjects: list[GameObject] = [
    btn_one,
    btn_two,
    btn_three,
    btn_four,
    btn_five,
    btn_six,
    btn_seven,
    btn_eight,
    btn_nine,
    btn_zero,
    btn_plus,
    btn_minus,
    btn_times,
    btn_divide,
    btn_power,
    btn_equal,
    text_answer
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for obj in gameobjects:
                if type(obj) == Button:
                    obj.click()

    screen.fill(color_white)

    text_answer.set_text(calculator.get_calc_str())

    for obj in gameobjects:
        obj.render()

    pygame.display.update()