#!/usr/bin/env python3
import random
from brain_games.scripts.main_module import welcome_user
from brain_games.scripts.main_module import question_prime
from brain_games.scripts.main_module import print_answer
from brain_games.scripts.main_module import comparison_prime
from brain_games.scripts.main_module import congratulation


def main():
    welcome_user()
    task()
    result()


def task():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def initial_data():
    num = random.randint(1, 113)
    question_prime(num)


def result():
    correct_answers = 0
    while correct_answers < 3:
        initial_data()
        print_answer()
        if comparison_prime() == 1:
            correct_answers += 1
        else:
            break
    if correct_answers == 3:
        congratulation()


if __name__ == '__main__':
    main()
