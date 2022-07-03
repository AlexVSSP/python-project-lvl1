import random
from brain_games.main_logic import game


def welcome_game_gcd():
    return 'Find the greatest common divisor of given numbers.'


def game_rules():
    list = []
    begin_range = 1
    end_range = 100
    first_num = random.randint(begin_range, end_range)
    second_num = random.randint(begin_range, end_range)
    list.append(str(first_num))
    list.append(str(second_num))
    input_line = " ".join(list)
    greatest_common_divisor = 1
    curr_divisor = 1
    while curr_divisor <= min(first_num, second_num):
        if (first_num % curr_divisor == 0) and (second_num % curr_divisor == 0):
            greatest_common_divisor = curr_divisor
            curr_divisor += 1
        else:
            curr_divisor += 1
    return [input_line, str(greatest_common_divisor)]


def main_game():
    game(welcome_game_gcd(), repeat_game_rules)


def repeat_game_rules():
    in_line, gcd = game_rules()
    return [in_line, gcd]
