"""
    Calculator program
"""


def calculate(first_number: int, second_number: int, choice: int) -> int:
    if choice not in ([1, 2, 3, 4]):
        raise ValueError('Enter valid option (1,2,3,4) only!')
    if choice == 1:
        return first_number + second_number
    if choice == 2:
        return first_number - second_number
    if choice == 3:
        return first_number * second_number
    if choice == 4:
        return first_number / second_number


print('''
    Select operation:
    1. Add
    2. Substraction
    3. Multiple
    4. Division''')

operation_choice = int(input('Enter Choice(1/2/3/4):'))
first_number = int(input('Enter firt number:'))
second_number = int(input('Enter second number:'))
answer = calculate(first_number, second_number, operation_choice)
print(f'Your answer is {answer}')
