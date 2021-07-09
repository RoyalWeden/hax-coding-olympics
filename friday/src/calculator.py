import numpy as np
import sys
from cmdinfo import CmdInfo
import extra_math

class Calculator:
    answer = 0
    saved_answer = 0
    cur_operator = ''
    show_help_msg = True
    show_power_off_msg = True

    help_info = CmdInfo(
        'Help',
        ['help', 'help (page #)'],
        "get help on commands",
        ["help", "help 3", "help 5"]
    )
    power_off_info = CmdInfo(
        'Power Off',
        ['off', 'stop', 'exit'],
        "powers off calculator",
        ["off", "exit"]
    )
    number_info = CmdInfo(
        'Number',
        ['(number)'],
        "sets number to calculator or use in calculation",
        ["5", "134"]
    )
    addition_info = CmdInfo(
        'Addition',
        ['+', 'add', 'plus'],
        "adds two numbers together",
        ["3 + 5", "1 plus 1"]
    )
    subtraction_info = CmdInfo(
        'Subtraction',
        ['-', 'subtract', 'minus'],
        "subtracts two numbers",
        ["5 - 9", "100 minus 15"]
    )
    multiplication_info = CmdInfo(
        'Multiplication',
        ['*', 'multiply', 'times', 'of'],
        "multiplies two numbers together",
        ["1 * 34", "13 times 15"]
    )
    division_info = CmdInfo(
        'Division',
        ['/', 'divide'],
        "divides two numbers.",
        ["2 / 6", "15 divide 124"]
    )
    exponent_info = CmdInfo(
        'Exponent',
        ['**', '^', 'exponent', 'power'],
        "set one number to the power of another",
        ["42 ** 2", "2 ^ 8"]
    )
    sqrt_info = CmdInfo(
        'Square Root',
        ['sqrt', 'squareroot'],
        "get the square root of a number",
        ["5 sqrt", "100 sqrt"]
    )
    root_info = CmdInfo(
        'Root',
        ['root'],
        "get the root of a number",
        ["3 root 8", "15 root 225"]
    )
    factorial_info = CmdInfo(
        'Factorial',
        ['!', 'factorial'],
        "get the factorial of a number",
        ["5 !", "10 factorial"]
    )
    sin_info = CmdInfo(
        'Sin',
        ['sin'],
        "get the trigonometric sin of a number",
        ["90 sin"]
    )
    cos_info = CmdInfo(
        'Cosine',
        ['cos', 'cosine'],
        "get the trigonometric cosine of a number",
        ["90 cos"]
    )
    tan_info = CmdInfo(
        'Tangent',
        ['tan', 'tangent'],
        "get the trigonometric tangent of a number",
        ["90 tan"]
    )
    show_help_msg_info = CmdInfo(
        'Show Help Message',
        ['show help msg'],
        "shows help message on calculator",
        ["show help msg"]
    )
    hide_help_msg_info = CmdInfo(
        'Hide Help Message',
        ['hide help msg'],
        "hides help message on calculator",
        ["hide help msg"]
    )
    show_power_off_msg_info = CmdInfo(
        'Show Power Off Message',
        ['show poweroff msg'],
        "shows power off message on calculator",
        ["show poweroff msg"]
    )
    hide_power_off_msg_info = CmdInfo(
        'Hide Power Off Message',
        ['hide poweroff msg'],
        "hides power off message on calculator",
        ["hide poweroff msg"]
    )

    cmdinfos = [
        help_info,
        power_off_info,
        number_info,
        addition_info,
        subtraction_info,
        multiplication_info,
        division_info,
        exponent_info,
        sqrt_info,
        root_info,
        factorial_info,
        sin_info,
        cos_info,
        tan_info,
        show_help_msg_info,
        show_power_off_msg_info,
        hide_help_msg_info,
        hide_power_off_msg_info
    ]

    def __init__(self):
        pass

    def calc_screen(self):
        return f"""
____________________________
|                          |
|  {' ' * (22-len(str(self.answer))) + str(self.answer)}  |
|__________________________|""" + (f"""
|                          |
|  {' ' * ((22-len(self.cur_operator)) // 2) + self.cur_operator + ' ' * ((22-len(self.cur_operator)) // 2 + (22-len(self.cur_operator)) % 2)}  |
|__________________________|
""" if self.cur_operator != '' else '\n') + \
("""|                          |
|     Don't know how to    |
|        perform a         |
|       calculation?       |
|__________________________|
|                          |
|    enter: help (pg #)    |
|__________________________|""" + \
('\n'  if self.show_power_off_msg else '') if self.show_help_msg else '') + \
("""|                          |
|   Power off calculator   |
|        enter: off        |
|__________________________|""" if self.show_power_off_msg else '')

    def check_enter(self, enter: str):
        if enter in self.power_off_info.enter_options:
            return False
        elif enter[:4] == 'help':
            page = enter[5:]
            self.get_help(int(page) if page.isdigit() else 1)
        elif enter.isnumeric() or \
            (enter.count('.')==1 and enter.replace('.', '').isnumeric()) or \
            (enter[0]=='-' and (enter[1:].isnumeric() or \
            enter[1:].count('.')==1 and enter[1:].replace('.', '').isnumeric())):
            if self.cur_operator != '':
                self.answer = self.operate(self.saved_answer, self.cur_operator, float(enter))
            else:
                self.answer = float(enter)
            self.cur_operator = ''
        elif 'hide' in enter or 'show' in enter:
            if enter in self.show_help_msg_info.enter_options:
                self.show_help_msg = True
            elif enter in self.hide_help_msg_info.enter_options:
                self.show_help_msg = False
            elif enter in self.show_power_off_msg_info.enter_options:
                self.show_power_off_msg = True
            elif enter in self.hide_power_off_msg_info.enter_options:
                self.show_power_off_msg = False
        else:
            self.saved_answer = self.answer
            if len(enter.split(' ')) > 1:
                for enteree in enter.split(' '):
                    self.check_enter(enteree)
            elif enter in self.addition_info.enter_options:
                self.cur_operator = 'add'
            elif enter in self.subtraction_info.enter_options:
                self.cur_operator = 'subtract'
            elif enter in self.multiplication_info.enter_options:
                self.cur_operator = 'multiply'
            elif enter in self.division_info.enter_options:
                self.cur_operator = 'divide'
            elif enter in self.exponent_info.enter_options:
                self.cur_operator = 'exponent'
            elif enter in self.sqrt_info.enter_options:
                self.cur_operator = 'sqrt'
                self.answer = self.operate(self.saved_answer, self.cur_operator)
            elif enter in self.root_info.enter_options:
                self.cur_operator = 'root'
            elif enter in self.factorial_info.enter_options:
                self.cur_operator = 'factorial'
                self.answer = self.operate(self.saved_answer, self.cur_operator)
            elif enter in self.sin_info.enter_options:
                self.cur_operator = 'sin'
                self.answer = self.operate(self.saved_answer, self.cur_operator)
            elif enter in self.cos_info.enter_options:
                self.cur_operator = 'cos'
                self.answer = self.operate(self.saved_answer, self.cur_operator)
            elif enter in self.tan_info.enter_options:
                self.cur_operator = 'tan'
                self.answer = self.operate(self.saved_answer, self.cur_operator)
        return True

    def operate(self, num1, operator, num2=0):
        try:
            self.cur_operator = ''
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
            elif operator == 'sqrt':
                return np.sqrt(num1)
            elif operator == 'root':
                return num2 ** (1 / num1)
            elif operator == 'factorial':
                if int(num1) == num1:
                    return extra_math.factorial(int(num1))
                else:
                    input("\nType Error: The number inputted needs to be an integer.\nPress enter to continue...")
                    return 0
            elif operator == 'sin':
                return np.sin(num1)
            elif operator == 'cos':
                return np.cos(num1)
            elif operator == 'tan':
                return np.tan(num1)
        except OverflowError:
            input("\nOverflow Error: The resulting value is too large.\nPress enter to continue...")
            return 0
        except ZeroDivisionError:
            input("\nZero Division Error: I think that would be infinity...don't do that...\nPress enter to continue...")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return 0

    def get_help(self, page):
        if page > int(np.ceil(len(self.cmdinfos)/3)):
            print(f"""
___________________________________________________________________________

                           Page does not exist
                          (Total Page Count: {int(np.ceil(len(self.cmdinfos)/3))})         
___________________________________________________________________________
""")
        else:
            print(f"""
___________________________________________________________________________

                            Help Page {page} of {int(np.ceil(len(self.cmdinfos)/3))}            
___________________________________________________________________________
___________________________________________________________________________
""")
        for i in range((page-1)*3, len(self.cmdinfos) if page*3>len(self.cmdinfos) else page*3):
                print(self.cmdinfos[i])
        input("Press enter to continue...")