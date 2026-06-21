from random import choice, randint


def banner():
    print('What is the result of the expression?')


def calculate(operation, arg1, arg2):
    match operation:
        case '+':
            return arg1 + arg2
        case '-':
            return arg1 - arg2
        case '*':
            return arg1 * arg2


def question_with_answer():
    operations = ['+', '-', '*']
    operation = choice(operations)
    arg1 = randint(1, 100)
    arg2 = randint(1, 100)
    answer = calculate(operation, arg1, arg2)
    return f'{arg1} {operation} {arg2}', str(answer)