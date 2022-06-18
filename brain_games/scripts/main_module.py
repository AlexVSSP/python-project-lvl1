#!/usr/bin/env python3
import prompt
import random


def welcome_user():
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def question_even(value):
    global number_even
    number_even = value
    print(f'Question: {value}')


def question_calc(text, value):
    global number_calc
    number_calc = value
    print(f'Question: {text}')


def print_answer():
    global answer
    answer = prompt.string('Your answer: ')


def comparison_even():
    if number_even % 2 == 0:
        if answer == 'yes':
            print('Correct!')
            return 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!""")
            return 0
    else:
        if answer == 'no':
            print('Correct!')
            return 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!""")
            return 0


def comparison_calc():
    if answer == str(number_calc):
        print('Correct!')
        return 1
    else:
        print(f"""'{answer}' is wrong answer ;(. Correct answer was '{number_calc}'.
Let's try again, {name}!""")
        return 0


def congratulation():
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
