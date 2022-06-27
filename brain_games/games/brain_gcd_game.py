#!/usr/bin/env python3
import random
from brain_games.main_logic import welcome_game
from brain_games.main_logic import check_answer


def welcome_game_gcd():
    welcome_game('Find the greatest common divisor of given numbers.')


def checking_data():
    for i in range(3):
        list = []
        first_num = random.randint(1, 100)
        second_num = random.randint(1, 100)
        list.append(str(first_num))
        list.append(str(second_num))
        input_line = " ".join(list)
        gcd = 1
        j = 1
        while j <= min(first_num, second_num):
            if (first_num % j == 0) and (second_num % j == 0):
                gcd = j
                j += 1
            else:
                j += 1
        if check_answer(input_line, str(gcd)) == 0:
            break
