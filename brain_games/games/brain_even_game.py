#!/usr/bin/env python3
import random
from brain_games.main_logic import welcome_game
from brain_games.main_logic import check_answer


def welcome_game_even():
    welcome_game('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(check_number):
    if check_number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def checking_data():
    for i in range(3):
        number = random.randint(1, 100)
        right_answer = is_even(number)
        if check_answer(number, right_answer) == 0:
            break
