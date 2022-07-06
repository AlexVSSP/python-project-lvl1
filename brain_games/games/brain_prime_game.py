import random
from brain_games.engine import game


WELCOME_GAME_PRIME = ("Answer 'yes' if given number is prime, "
                      "otherwise answer 'no'.")
BEGIN_RANGE = 2
END_RANGE = 113


def is_prime(check_number):
    number_of_divisors = 0
    current_number = 1
    while current_number <= check_number:
        if check_number % current_number == 0:
            number_of_divisors += 1
        current_number += 1
    if number_of_divisors == 2:
        return True
    else:
        return False


def game_rules():
    number = random.randint(BEGIN_RANGE, END_RANGE)
    if is_prime(number) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return [number, right_answer]


def main_game():
    game(WELCOME_GAME_PRIME, game_rules)
