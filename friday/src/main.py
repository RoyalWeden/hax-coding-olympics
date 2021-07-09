from calculator import Calculator

is_calc_on = True

if __name__ == '__main__':
    calc = Calculator()

    while is_calc_on:
        print(calc.calc_screen())
        enter = input('\n: ').lower()
        is_calc_on = calc.check_enter(enter)