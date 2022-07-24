import random
from brain_games.engine import play_game


WELCOME_GAME_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'
BEGIN_RANGE = 1
END_RANGE = 100


def is_even(check_number):
    if check_number % 2 == 0:
        return True
    else:
        return False


def generate_round_parametres():
    number = random.randint(BEGIN_RANGE, END_RANGE)
    if is_even(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return number, right_answer


def start_game():
    play_game(WELCOME_GAME_EVEN, generate_round_parametres)
