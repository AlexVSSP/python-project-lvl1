import random
from brain_games.engine import play_game
from math import sqrt


WELCOME_GAME_PRIME = ("Answer 'yes' if given number is prime, "
                      "otherwise answer 'no'.")
BEGIN_RANGE = 2
END_RANGE = 113


def is_prime(check_number):
    current_number = 2
    while current_number <= int(sqrt(check_number)) + 1:
        if check_number % current_number == 0:
            return False
        else:
            current_number += 1
    return True


def generate_round_parametres():
    number = random.randint(BEGIN_RANGE, END_RANGE)
    if is_prime(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return [number, right_answer]


def start_game():
    play_game(WELCOME_GAME_PRIME, generate_round_parametres)
