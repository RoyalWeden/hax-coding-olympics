import numpy as np
import sys
from cmdinfo import CmdInfo
import cmdinfos
import extra_math

class Calculator:
    answer = 0
    saved_answer = 0
    cur_operator = ''
    show_help_msg = True
    show_power_off_msg = True
    is_degree = True

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
|  enter: help (# or func) |
|__________________________|""" + \
('\n'  if self.show_power_off_msg else '') if self.show_help_msg else '') + \
("""|                          |
|   Power off calculator   |
|        enter: off        |
|__________________________|""" if self.show_power_off_msg else '')

    def check_enter(self, enter: str):
        if enter[:4] == 'help':
            page = enter[5:]
            if page.isnumeric() or page == '':
                self.get_help(int(page) if page.isdigit() else 1)
            else:
                for cmdinfo in cmdinfos.cmdinfos:
                    if page in cmdinfo.enter_options:
                        print()
                        print(cmdinfo)
                        input("Press enter to continue...")
        elif enter in cmdinfos.power_off_info.enter_options:
            return False
        elif enter[:7] == 'setting':
            self.get_settings()
        elif enter in cmdinfos.clear_info.enter_options:
            self.answer = self.saved_answer = 0
            self.cur_operator = ''
        elif enter in cmdinfos.reset_info.enter_options:
            self.show_help_msg = True
            self.show_power_off_msg = True
            self.check_enter('clear')
        elif enter.isnumeric() or \
            (enter.count('.')==1 and enter.replace('.', '').isnumeric()) or \
            (enter[0]=='-' and (enter[1:].isnumeric() or \
            enter[1:].count('.')==1 and enter[1:].replace('.', '').isnumeric())) or \
            enter == 'e' or enter == 'pi':
            if self.cur_operator != '':
                self.answer = self.operate(self.saved_answer, self.cur_operator, extra_math.get_math_val(enter))
            else:
                self.answer = extra_math.get_math_val(enter)
            self.cur_operator = ''
        elif enter[0:4] == 'hide' or enter[0:4] == 'show':
            if enter in cmdinfos.show_help_msg_info.enter_options:
                self.show_help_msg = True
            elif enter in cmdinfos.hide_help_msg_info.enter_options:
                self.show_help_msg = False
            elif enter in cmdinfos.show_power_off_msg_info.enter_options:
                self.show_power_off_msg = True
            elif enter in cmdinfos.hide_power_off_msg_info.enter_options:
                self.show_power_off_msg = False
        elif enter[0:4] == 'mode':
            which_mode = enter[5:]
            if which_mode[0:3] == 'deg':
                self.is_degree = True
            elif which_mode[0:3] == 'rad':
                self.is_degree = False
            else:
                if self.is_degree:
                    self.is_degree = False
                else:
                    self.is_degree = True
        else:
            self.saved_answer = self.answer
            if len(enter.split(' ')) > 1:
                for enteree in enter.split(' '):
                    self.check_enter(enteree)
            elif enter in cmdinfos.addition_info.enter_options:
                self.cur_operator = 'add'
            elif enter in cmdinfos.subtraction_info.enter_options:
                self.cur_operator = 'subtract'
            elif enter in cmdinfos.multiplication_info.enter_options:
                self.cur_operator = 'multiply'
            elif enter in cmdinfos.division_info.enter_options:
                self.cur_operator = 'divide'
            elif enter in cmdinfos.exponent_info.enter_options:
                self.cur_operator = 'exponent'
            elif enter in cmdinfos.sqrt_info.enter_options:
                self.cur_operator = 'sqrt'
                self.answer = self.operate(self.saved_answer, self.cur_operator)
            elif enter in cmdinfos.root_info.enter_options:
                self.cur_operator = 'root'
            elif enter in cmdinfos.factorial_info.enter_options:
                self.cur_operator = 'factorial'
                self.answer = self.operate(self.saved_answer, self.cur_operator)
            elif enter in cmdinfos.sin_info.enter_options:
                self.cur_operator = 'sin'
                self.answer = self.operate(self.saved_answer, self.cur_operator)
            elif enter in cmdinfos.cos_info.enter_options:
                self.cur_operator = 'cos'
                self.answer = self.operate(self.saved_answer, self.cur_operator)
            elif enter in cmdinfos.tan_info.enter_options:
                self.cur_operator = 'tan'
                self.answer = self.operate(self.saved_answer, self.cur_operator)
            elif enter in cmdinfos.natural_log_info.enter_options:
                self.cur_operator = 'ln'
                self.answer = self.operate(self.saved_answer, self.cur_operator)
            elif enter in cmdinfos.log_info.enter_options:
                self.cur_operator = 'log'
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
            elif operator == 'sin' or operator == 'cos' or operator == 'tan':
                return extra_math.get_trig(num1, operator, self.is_degree)
            elif operator == 'ln':
                if num1 == 0:
                    raise ZeroDivisionError
                return np.log(num1)
            elif operator == 'log':
                return np.log(num1) / np.log(num2)
        except OverflowError:
            input("\nOverflow Error: The resulting value is too large.\nPress enter to continue...")
            return 0
        except ZeroDivisionError:
            input("\nZero Division Error: I think that would be infinity...don't do that...\nPress enter to continue...")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return 0

    def get_help(self, page):
        if page > int(np.ceil(len(cmdinfos.cmdinfos)/3)):
            print(f"""
___________________________________________________________________________

                           Page does not exist
                          (Total Page Count: {int(np.ceil(len(cmdinfos.cmdinfos)/3))})         
___________________________________________________________________________
""")
        else:
            print(f"""
___________________________________________________________________________

                            Help Page {page} of {int(np.ceil(len(cmdinfos.cmdinfos)/3))}            
___________________________________________________________________________
___________________________________________________________________________
""")
        for i in range((page-1)*3, len(cmdinfos.cmdinfos) if page*3>len(cmdinfos.cmdinfos) else page*3):
                print(cmdinfos.cmdinfos[i])
        input("Press enter to continue...")

    def get_settings(self):
        setting_mode = 'degree' if self.is_degree else 'radian'
        setting_help_msg = 'on' if self.show_help_msg else 'off'
        setting_power_msg = 'on' if self.show_power_off_msg else 'off'
        print(f"""
___________________________________________________________________________

                                Settings
                    Mode:                   {setting_mode}
                    Help Message:           {setting_help_msg}
                    Power Off Message:      {setting_power_msg}
___________________________________________________________________________
""")
        input("Press enter to continue...")