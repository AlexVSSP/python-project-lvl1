#!/usr/bin/env python3
import random
from brain_games.main_logic import welcome_game
from brain_games.main_logic import check_answer


def welcome_game_prime():
    welcome_game(
        'Answer "yes" if given number is prime, '
        'otherwise answer "no".')


def is_prime(check_number):
    i = 0
    current_number = 1
    while current_number <= check_number:
        if check_number % current_number == 0:
            i += 1
        current_number += 1
    if i == 2:
        return 'yes'
    else:
        return 'no'


def checking_data():
    for i in range(3):
        number = random.randint(2, 113)
        right_answer = is_prime(number)
        if check_answer(number, right_answer) == 0:
            break
