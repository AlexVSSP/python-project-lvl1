import random
from brain_games.main_logic import game


def welcome_game_progression():
    return 'What number is missing in the progression?'


def game_rules():
    begin_range_first_num = 1
    end_range_first_num = 20
    begin_range_step = 2
    end_range_step = 9
    first_num = random.randint(begin_range_first_num, end_range_first_num)
    step = random.randint(begin_range_step, end_range_step)
    i = 0
    list = []
    total_numbers = 10
    while i < total_numbers:
        list.append(str(first_num))
        first_num += step
        i += 1
    begin_range_targ_ind = 0
    end_range_targ_ind = 9
    target_index = random.randint(begin_range_targ_ind, end_range_targ_ind)
    target_value = list[target_index]
    list[target_index] = '..'
    input_line = " ".join(list)
    return [input_line, str(target_value)]


def main_game():
    game(welcome_game_progression(), repeat_game_rules)


def repeat_game_rules():
    in_line, target_val = game_rules()
    return [in_line, target_val]
