#!/usr/bin/env python3
import random
from brain_games.main_logic import welcome_game
from brain_games.main_logic import check_answer


def welcome_game_progression():
    welcome_game('What number is missing in the progression?')


def checking_data():
    for i in range(3):
        first_num = random.randint(1, 20)
        step = random.randint(2, 9)
        i = 0
        list = []
        while i < 10:
            list.append(str(first_num))
            first_num += step
            i += 1
        target_index = random.randint(0, 9)
        target_value = list[target_index]
        list[target_index] = '..'
        input_line = " ".join(list)
        if check_answer(input_line, str(target_value)) == 0:
            break
