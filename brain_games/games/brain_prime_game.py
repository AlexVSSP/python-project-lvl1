import random
from brain_games.main_logic import game


def welcome_game_prime():
    return ("Answer 'yes' if given number is prime, "
            "otherwise answer 'no'.")


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


def game_rules(checking_func):
    begin_range = 2
    end_range = 113
    number = random.randint(begin_range, end_range)
    if checking_func(number) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return [number, right_answer]


def main_game():
    game(welcome_game_prime(), repeat_game_rules)


def repeat_game_rules():
    numb, answ = game_rules(is_prime)
    return [numb, answ]
