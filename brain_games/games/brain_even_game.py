import random
from brain_games.main_logic import game


def welcome_game_even():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(check_number):
    if check_number % 2 == 0:
        return True
    else:
        return False


def game_rules(checking_func):
    begin_range = 1
    end_range = 100
    number = random.randint(begin_range, end_range)
    if checking_func(number) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return [number, right_answer]


def main_game():
    game(welcome_game_even(), repeat_game_rules)


def repeat_game_rules():
    numb, answ = game_rules(is_even)
    return [numb, answ]
