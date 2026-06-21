from random import randint

PROGRESSION_START_BOUNDARY = 20
MAX_STEP = 10


def banner():
    print('What number is missing in the progression?')


def make_progression(length):
    first = randint(1, PROGRESSION_START_BOUNDARY)
    step = randint(1, MAX_STEP)
    return [str(first + x * step) for x in range(length)]


def question_with_answer():
    length = 10
    progression = make_progression(length)
    hide_index = randint(0, length - 1)
    answer = progression[hide_index]
    progression[hide_index] = '..'
    return ' '.join(progression), answer