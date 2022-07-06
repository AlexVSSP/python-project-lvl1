import random
from brain_games.engine import game


WELCOME_GAME_GCD = 'Find the greatest common divisor of given numbers.'
BEGIN_RANGE = 1
END_RANGE = 100


def game_rules():
    list = []
#    begin_range = 1
#    end_range = 100
    first_num = random.randint(BEGIN_RANGE, END_RANGE)
    second_num = random.randint(BEGIN_RANGE, END_RANGE)
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
    game(WELCOME_GAME_GCD, game_rules)
