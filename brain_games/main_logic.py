import prompt


def game(game_rule, game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_rule)
    max_stages = 3
    correct_answers = 0
    req_number_correct_answers = 3
    for i in range(max_stages):
        number, answer = game()
        print(f'Question: {number}')
        response = prompt.string('Your answer: ')
        if response == answer:
            print('Correct!')
            correct_answers += 1
            game()
        else:
            print(f"""'{response}' is wrong answer ;(. Correct answer was '{answer}'.
Let's try again, {name}!""")
            break
        if correct_answers == req_number_correct_answers:
            print(f'Congratulations, {name}!')
