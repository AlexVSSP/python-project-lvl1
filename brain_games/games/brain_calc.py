#!/usr/bin/env python3
import prompt
import random
from brain_games.scripts.main_module import welcome_user
from brain_games.scripts.main_module import question_calc
from brain_games.scripts.main_module import print_answer
from brain_games.scripts.main_module import comparison_calc
from brain_games.scripts.main_module import congratulation

def main():
    welcome_user()
    task()
    result()


def task():
    print('What is the result of the expession?')


def initial_data():
    first_num = random.randint(1, 50)
    second_num = random.randint(1, 20)
    operation = random.choice(['+', '-', '*'])
    expression = f'{str(first_num)} {operation} {str(second_num)}'
    if operation == '+':
        calc = first_num + second_num
    elif operation == '-':
        calc = first_num - second_num
    elif operation == '*':
        calc = first_num * second_num
    question_calc(expression, calc)


def result():
    correct_answers = 0
    while correct_answers < 3:
        initial_data()
        print_answer()
        if comparison_calc() == 1:
            correct_answers +=1
        else:
            break
    if correct_answers == 3:
        congratulation()


if __name__ == '__main__':
    main()
