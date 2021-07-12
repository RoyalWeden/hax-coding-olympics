import numpy as np
import time

class Calculator:
    ans = 0
    calculation = []
    operations = [
        '+',
        '-',
        '*',
        '/',
        '^',
        '√',
        ' √'
    ]

    def __init__(self):
        pass

    def enter(self, x):
        self.calculation.append(x)
        print(f'Entered: {x}')

    def calculate(self):
        answer = x = 0
        if len(self.calculation) == 0:
            self.ans = self.ans
            return
        elif self.calculation[0] in self.operations:
            num1 = self.ans
            operator = self.calculation[0]
            x = 1
            if x < len(self.calculation) and \
                (type(self.calculation[x]) == int or self.calculation[x] == 'π' or self.calculation[x] == 'e'):
                if self.calculation[x] == 'π':
                    num2 = np.pi
                elif self.calculation[x] == 'e':
                    num2 = np.e
                else:
                    num2 = self.calculation[x]
                    while len(self.calculation) > x and type(self.calculation[x]) == int:
                        num2 = int(str(num2) + str(self.calculation[x]))
                        x += 1
                answer = self.operate(num1, operator, num2)
        while x < len(self.calculation):
            if type(self.calculation[x]) == int or self.calculation[x] == 'π' or self.calculation[x] == 'e':
                i = x + 1
                if self.calculation[x] == 'π':
                    num1 = np.pi
                elif self.calculation[x] == 'e':
                    num1 = np.e
                else:
                    num1 = self.calculation[x]
                    while len(self.calculation) > i and type(self.calculation[i]) == int:
                        num1 = int(str(num1) + str(self.calculation[i]))
                        i += 1
                if len(self.calculation) > i:
                    operator = self.calculation[i]
                    i += 1
                    if len(self.calculation) > i and \
                        (type(self.calculation[i]) == int or self.calculation[i] == 'π' or self.calculation[i] == 'e'):
                        if self.calculation[i] == 'π':
                            num2 = np.pi
                            i += 1
                        elif self.calculation[i] == 'e':
                            num2 = np.e
                            i += 1
                        else:
                            num2 = self.calculation[i]
                            i += 1
                            while len(self.calculation) > i and  type(self.calculation[i]) == int:
                                num2 = int(str(num2) + str(self.calculation[i]))
                                i += 1
                    else:
                        num2 = None
                else:
                    operator = None
                    num2 = None
                x = i
            else:
                num1 = answer
                operator = self.calculation[x]
                num2 = None if x+1==len(self.calculation) else self.calculation[x+1]
            answer = self.operate(num1, operator, num2)
            
        self.ans = answer
        self.calculation = []
        print(f'Calculated: {self.ans}')

    def operate(self, num1: float, operation: str, num2: float):
        try:
            if operation==None:
                return num1

            if num2==None:
                return num1
            
            if operation=='+':
                return num1+num2
            if operation=='-':
                return num1-num2
            if operation=='*':
                return num1*num2
            if operation=='/':
                return num1/num2
            if operation=='^':
                return num1**num2
            if operation=='√':
                return num1*np.sqrt(num2)
            if operation==' √':
                return num2**(1/num1)

        except ZeroDivisionError:
            print('Error: Divide by zero')
        except ValueError:
            print('Error: Value wrong type')
        except OverflowError:
            print('Error: Value too large')
        except:
            print('Unexpected error')
        return num1

    def get_calc_str(self):
        return str(self.ans) \
            if len(self.calculation)==0 \
                else ('ANS ' if self.calculation[0] in self.operations else '') + \
                    ' '.join([str(x) for x in self.calculation]).replace('  ', ' ')