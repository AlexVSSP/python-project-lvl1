import prompt


REQ_NUMBER_CORRECT_ANSWERS = 3


def play_game(game_rule, game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_rule)
    correct_answers = 0
    for i in range(REQ_NUMBER_CORRECT_ANSWERS):
        number, answer = game()
        print(f'Question: {number}')
        response = prompt.string('Your answer: ')
        if response == answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"""'{response}' is wrong answer ;(. Correct answer was '{answer}'.
Let's try again, {name}!""")
            break
    else:
        print(f'Congratulations, {name}!')
