from math import sqrt
from random import randint

MAX_NUMBER = 100


def banner():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(number):
    print('checking prime')
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def question_with_answer():
    number = randint(1, MAX_NUMBER)
    answer = 'yes' if is_prime(number) else 'no'
    return number, answer