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


def question_gcd(number1, number2):
    global num1, num2
    num1 = number1
    num2 = number2
    print(f'Question: {number1} {number2}')


def question_progression(in_first_num, in_step):
    global target_value
    i = 0
    list = []
    target_value = 0
    target_index = 0
    while i < 10:
        list.append(str(in_first_num))
        in_first_num += in_step
        i += 1
    target_index = random.randint(0, 9)
    target_value = list[target_index]
    list[target_index] = '..'
    in_line = " ".join(list)
    print('Question:', in_line)


def question_prime(in_number):
    global number_prime
    number_prime = in_number
    print(f'Question: {in_number}')


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


def comparison_gcd():
    gcd = 1
    i = 1
    while i <= min(num1, num2):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd = i
            i += 1
        else:
            i += 1
    if answer == str(gcd):
        print('Correct!')
        return 1
    else:
        print(f"""'{answer}' is wrong answer ;(. Correct answer was '{gcd}'.
Let's try again, {name}!""")
        return 0


def comparison_progression():
    if answer == str(target_value):
        print('Correct!')
        return 1
    else:
        print(f"""'{answer}' is wrong answer ;(. Correct answer was '{target_value}'.
Let's try again, {name}!""")


def comparison_prime():
    i = 0
    current_number = 1
    while current_number <= number_prime:
        if (number_prime % current_number == 0):
            i += 1
        current_number += 1
    if i == 2:
        if answer == 'yes':
            print('Correct!')
            return 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!""")
    else:
        if answer == 'no':
            print('Correct!')
            return 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!""")


def congratulation():
    print(f'Congratulations, {name}!')


# if __name__ == '__main__':
#    main()
