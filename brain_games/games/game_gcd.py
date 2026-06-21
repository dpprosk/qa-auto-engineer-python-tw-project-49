from math import gcd
from random import randint

MAX_NUMBER = 100


def banner():
    print('Find the greatest common divisor of given numbers.')


def question_with_answer():
    first_number = randint(1, MAX_NUMBER)
    second_number = randint(1, MAX_NUMBER)
    answer = gcd(first_number, second_number)
    return f'{first_number} {second_number}', str(answer)