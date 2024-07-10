def play_game(description, generate_question_and_answer):
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')

    print(description)
    correct_answers_needed = 3
    correct_answers_given = 0

    while correct_answers_given < correct_answers_needed:
        question, correct_answer = generate_question_and_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ').strip()

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers_given += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
