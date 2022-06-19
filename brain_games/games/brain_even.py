#!/usr/bin/env python3
import random
from brain_games.scripts.main_module import welcome_user
from brain_games.scripts.main_module import question_even
from brain_games.scripts.main_module import print_answer
from brain_games.scripts.main_module import comparison_even
from brain_games.scripts.main_module import congratulation


def main():
    welcome_user()
    task()
    result()


def task():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def initial_data():
    range = random.randint(1, 100)
    question_even(range)


def result():
    correct_answers = 0
    while correct_answers < 3:
        initial_data()
        print_answer()
        if comparison_even() == 1:
            correct_answers += 1
        else:
            break
    if correct_answers == 3:
        congratulation()


if __name__ == '__main__':
    main()
