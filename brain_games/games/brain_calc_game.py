import random
from brain_games.main_logic import game


def welcome_game_calc():
    return 'What is the result of the expression?'


def game_rules():
    begin_range = 1
    end_range_first_num = 50
    end_range_second_num = 20
    first_num = random.randint(begin_range, end_range_first_num)
    second_num = random.randint(begin_range, end_range_second_num)
    operation = random.choice(['+', '-', '*'])
    expression = f'{str(first_num)} {operation} {str(second_num)}'
    if operation == '+':
        result = first_num + second_num
    elif operation == '-':
        result = first_num - second_num
    elif operation == '*':
        result = first_num * second_num
    return [expression, str(result)]


def main_game():
    game(welcome_game_calc(), repeat_game_rules)


def repeat_game_rules():
    expr, res = game_rules()
    return [expr, res]
