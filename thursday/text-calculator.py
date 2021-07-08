import numpy as np

answer = 0
saved_answer = 0
is_calc_on = True
cur_operator = ''

def calc_screen():
    return f"""
____________________________
|                          |
|  {' ' * (22-len(str(answer))) + str(answer)}  |
|__________________________|""" + (f"""
|                          |
|  {' ' * ((22-len(cur_operator)) // 2) + cur_operator + ' ' * ((22-len(cur_operator)) // 2 + (22-len(cur_operator)) % 2)}  |
|__________________________|
""" if cur_operator != '' else '\n') + """|                          |
|     Don't know how to    |
|        perform a         |
|       calculation?       |
|__________________________|
|                          |
|    enter: help (pg #)    |
|__________________________|
"""

def check_enter(enter: str):
    global is_calc_on
    global answer
    global saved_answer
    global cur_operator

    if enter == 'off' or enter == 'stop' or enter == 'exit':
        is_calc_on = False
    elif enter[:4] == 'help':
        page = enter[5:]
        get_help(int(page) if page.isdigit() else 1)
    elif enter.isnumeric() or (enter.count('.') == 1 and enter.replace('.', '').isnumeric()):
        if cur_operator != '':
            answer = operate(saved_answer, cur_operator, float(enter))
        else:
            answer = float(enter)
        cur_operator = ''
    else:
        if enter == '+' or enter == 'add':
            cur_operator = 'add'
            saved_answer = answer
        elif enter == '-' or enter == 'subtract':
            cur_operator = 'subtract'
            saved_answer = answer
        elif enter == '*' or enter == 'multiply':
            cur_operator = 'multiply'
            saved_answer = answer
        elif enter == '/' or enter == 'divide':
            cur_operator = 'divide'
            saved_answer = answer
        elif enter == '**' or enter == '^' or enter == 'exponent':
            cur_operator = 'exponent'
            saved_answer = answer

def operate(num1, operator, num2):
    if operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2
    elif operator == 'multiply':
        return num1 * num2
    elif operator == 'divide':
        return num1 / num2
    elif operator == 'exponent':
        return num1 ** num2


def get_help(page):
    if page == 1:
        print("""
__________________________________________

               Help Page #1               
__________________________________________

  Addition:
------------------------------------------
  enter: '+' or 'add'


  Subtraction:
------------------------------------------
  enter: '-' or 'subtract'


  Multiplication:
------------------------------------------
  enter: '*' or 'multiply'


  Division:
------------------------------------------
  enter: '/' or 'divide'
        """)
    elif page == 2:
        print("""
__________________________________________

               Help Page #2               
__________________________________________

  Exponent:
------------------------------------------
  enter: '**' or '^' or 'exponent'


  Operation:
------------------------------------------
  enter: stuff


  Operation:
------------------------------------------
  enter: stuff


  Operation:
------------------------------------------
  enter: stuff
        """)
    else:
        print("""
        Page does not exist.
        """)
    input("Press enter to continue...")




if __name__ == '__main__':
    while is_calc_on:
        print(calc_screen())
        enter = input(': ').lower()
        check_enter(enter)