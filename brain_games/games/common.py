import prompt

from . import game_calc, game_even


def print_banner(game):
    match game:
        case 'even':
            game_even.banner()
        case 'calc':
            game_calc.banner()


def get_data(game):
    match game:
        case 'even':
            return game_even.question_with_answer()
        case 'calc':
            return game_calc.question_with_answer()


def start(game):
    max_correct_answers = 3
    correct_answers_count = 0
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    print_banner(game)
    while correct_answers_count < max_correct_answers:
        question, correct_answer = get_data(game)
        answer = prompt.string(f'Question: {question}\nYour answer: ')
        if answer == correct_answer:
            correct_answers_count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            break
    if correct_answers_count == max_correct_answers:
        print(f'Congratulations, {player_name}!')