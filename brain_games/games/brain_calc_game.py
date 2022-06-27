#!/usr/bin/env python3
import random
from brain_games.main_logic import welcome_game
from brain_games.main_logic import check_answer


def welcome_game_calc():
    welcome_game('What is the result of the expression?')


def checking_data():
    for i in range(3):
        first_num = random.randint(1, 50)
        second_num = random.randint(1, 20)
        operation = random.choice(['+', '-', '*'])
        expression = f'{str(first_num)} {operation} {str(second_num)}'
        if operation == '+':
            result = first_num + second_num
        elif operation == '-':
            result = first_num - second_num
        elif operation == '*':
            result = first_num * second_num
        if check_answer(expression, str(result)) == 0:
            break
