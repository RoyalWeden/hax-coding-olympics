import numpy as np
from cmdinfo import CmdInfo

class Calculator:
    answer = 0
    saved_answer = 0
    cur_operator = ''
    show_help_msg = True
    show_power_off_msg = True

    help_info = CmdInfo(
        'Help',
        ['help', 'help (page #)'],
        "get help on commands"
    )
    power_off_info = CmdInfo(
        'Power Off',
        ['off', 'stop', 'exit'],
        "powers off calculator"
    )
    addition_info = CmdInfo(
        'Addition',
        ['+', 'add'],
        "adds two numbers together"
    )
    subtraction_info = CmdInfo(
        'Subtraction',
        ['-', 'subtract'],
        "subtracts two numbers"
    )
    multiplication_info = CmdInfo(
        'Multiplication',
        ['*', 'multiply'],
        "multiplies two numbers together"
    )
    division_info = CmdInfo(
        'Division',
        ['/', 'divide'],
        "divides two numbers."
    )
    exponent_info = CmdInfo(
        'Exponent',
        ['**', '^', 'exponent', 'power'],
        "set one number to the power of another"
    )
    show_help_msg_info = CmdInfo(
        'Show Help Message',
        ['show help msg'],
        "shows help message on calculator"
    )
    hide_help_msg_info = CmdInfo(
        'Hide Help Message',
        ['hide help msg'],
        "hides help message on calculator"
    )
    show_power_off_msg_info = CmdInfo(
        'Show Power Off Message',
        ['show poweroff msg'],
        "shows power off message on calculator"
    )
    hide_power_off_msg_info = CmdInfo(
        'Hide Power Off Message',
        ['hide poweroff msg'],
        "hides power off message on calculator"
    )

    cmdinfos = [
        help_info,
        addition_info,
        subtraction_info,
        multiplication_info,
        division_info,
        exponent_info,
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
        elif enter.isnumeric() or (enter.count('.') == 1 and enter.replace('.', '').isnumeric()):
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
            if enter in self.addition_info.enter_options:
                self.cur_operator = 'add'
                self.saved_answer = self.answer
            elif enter in self.subtraction_info.enter_options:
                self.cur_operator = 'subtract'
                self.saved_answer = self.answer
            elif enter in self.multiplication_info.enter_options:
                self.cur_operator = 'multiply'
                self.saved_answer = self.answer
            elif enter in self.division_info.enter_options:
                self.cur_operator = 'divide'
                self.saved_answer = self.answer
            elif enter in self.exponent_info.enter_options:
                self.cur_operator = 'exponent'
                self.saved_answer = self.answer
        return True

    def operate(self, num1, operator, num2):
        try:
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
        except OverflowError:
            input("\nError: The resulting value is too large.\nPress enter to continue...")
            return 0
        except:
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
""")
        for i in range((page-1)*3, len(self.cmdinfos) if page*3>len(self.cmdinfos) else page*3):
                print(self.cmdinfos[i])
        input("Press enter to continue...")