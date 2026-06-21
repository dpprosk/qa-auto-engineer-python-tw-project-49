from random import randint

MAX_NUMBER = 1000


def banner():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number):
    return number % 2 == 0


def question_with_answer():
    question = randint(1, MAX_NUMBER)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer