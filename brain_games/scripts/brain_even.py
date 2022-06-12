#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    question()


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')


def question():
    correct_answers = 0
    while correct_answers < 3:
        range = random.randint(1, 100)
        print(f'Question: {range}')
        answer = prompt.string('Your answer: ')
        if range % 2 == 0:
            if answer == 'yes':
                correct_answers += 1
                print('Correct!')
            else:
                print(f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!""")
                return
        else:
            if answer == 'no':
                correct_answers += 1
                print('Correct!')
            else:
                print(f"""'{answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!""")
                return
    if correct_answers == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
