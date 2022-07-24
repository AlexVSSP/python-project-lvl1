import random
from brain_games.engine import play_game


WELCOME_GAME_PROGRESSION = 'What number is missing in the progression?'
BEGIN_RANGE_FIRST_NUM = 1
END_RANGE_FIRST_NUM = 20
BEGIN_RANGE_STEP = 2
END_RANGE_STEP = 9
TOTAL_NUMBERS = 10
BEGIN_RANGE_TARG_IND = 0
END_RANGE_TARG_IND = 9


def generate_round_parametres():
    first_num = random.randint(BEGIN_RANGE_FIRST_NUM, END_RANGE_FIRST_NUM)
    step = random.randint(BEGIN_RANGE_STEP, END_RANGE_STEP)
    i = 0
    list = []
    while i < TOTAL_NUMBERS:
        list.append(str(first_num))
        first_num += step
        i += 1
    target_index = random.randint(BEGIN_RANGE_TARG_IND, END_RANGE_TARG_IND)
    target_value = list[target_index]
    list[target_index] = '..'
    input_line = " ".join(list)
    return input_line, str(target_value)


def start_game():
    play_game(WELCOME_GAME_PROGRESSION, generate_round_parametres)
