#!/usr/bin/env python3
import random
from brain_games.scripts.main_module import welcome_user
from brain_games.scripts.main_module import question_progression
from brain_games.scripts.main_module import print_answer
from brain_games.scripts.main_module import comparison_progression
from brain_games.scripts.main_module import congratulation


def main():
    welcome_user()
    task()
    result()


def task():
    print('What number is missing in the progression?')


def initial_data():
    first_num = random.randint(1, 20)
    step = random.randint(2, 9)
    question_progression(first_num, step)


def result():
    correct_answers = 0
    while correct_answers < 3:
        initial_data()
        print_answer()
        if comparison_progression() == 1:
            correct_answers += 1
        else:
            break
    if correct_answers == 3:
        congratulation()


if __name__ == '__main__':
    main()
