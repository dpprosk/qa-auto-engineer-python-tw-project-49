import prompt
from random import randint


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even(number):
    return number % 2 == 0


def get_correct_answer(number):
    if is_even(number):
        return 'yes'
    return 'no'


def start_even():
    player_name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    max_correct_answers = 3
    correct_answers_count = 0
    while correct_answers_count < max_correct_answers:
        number = randint(1, 1000)
        correct_answer = get_correct_answer(number)
        answer = prompt.string(f'Question: {number}\nYour answer: ')
        if answer == correct_answer:
            correct_answers_count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            break
    if correct_answers_count == max_correct_answers:
        print(f'Congratulations, {player_name}!')