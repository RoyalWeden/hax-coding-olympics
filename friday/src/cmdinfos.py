from cmdinfo import CmdInfo

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
clear_info = CmdInfo(
    'Clear',
    ['clear', 'cls'],
    "sets the calculator to 0",
    ["clear", "cls"]
)
reset_info = CmdInfo(
    'Reset',
    ['reset'],
    "resets the calculator to default settings",
    ['reset']
)
number_info = CmdInfo(
    'Number',
    ['(number)'],
    "sets number to calculator or use in calculation",
    ["5", "134"]
)
other_numbers_info = CmdInfo(
    'Other Numbers',
    ['e', 'pi'],
    "set or use these other numbers in calculator",
    ["e", "pi"]
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
natural_log_info = CmdInfo(
    'Natural Logarithm',
    ['ln', 'naturallog', 'loge'],
    "get the natural log of a number",
    ["e ln"]
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
    clear_info,
    reset_info,
    number_info,
    other_numbers_info,
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