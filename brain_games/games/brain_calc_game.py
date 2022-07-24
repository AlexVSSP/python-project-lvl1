import random
from brain_games.engine import play_game


WELCOME_GAME_CALC = 'What is the result of the expression?'
BEGIN_RANGE = 1
END_RANGE_FIRST_NUM = 50
END_RANGE_SECOND_NUM = 20


def generate_round_parametres():
    first_num = random.randint(BEGIN_RANGE, END_RANGE_FIRST_NUM)
    second_num = random.randint(BEGIN_RANGE, END_RANGE_SECOND_NUM)
    operation = random.choice(['+', '-', '*'])
    expression = f'{str(first_num)} {operation} {str(second_num)}'
    if operation == '+':
        result = first_num + second_num
    elif operation == '-':
        result = first_num - second_num
    elif operation == '*':
        result = first_num * second_num
    return expression, str(result)


def start_game():
    play_game(WELCOME_GAME_CALC, generate_round_parametres)
