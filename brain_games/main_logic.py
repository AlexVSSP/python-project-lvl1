#!/usr/bin/env python3
import prompt


def welcome_user():
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def welcome_game(task):
    print(task)


def question(expression):
    print(f'Question: {expression}')


def answer():
    global response
    response = prompt.string('Your answer: ')


correct_answers = 0


def check_answer(question_value, correct_answer):
    global correct_answers
    question(question_value)
    answer()
    if response == correct_answer:
        print('Correct!')
        correct_answers += 1
        if correct_answers == 3:
            print(f'Congratulation, {name}!')
        return 1
    else:
        print(f"""'{response}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
        return 0
