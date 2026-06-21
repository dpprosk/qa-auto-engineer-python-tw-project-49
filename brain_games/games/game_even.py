from random import randint


def banner():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number):
    return number % 2 == 0


def question_with_answer():
    question = randint(1, 1000)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer