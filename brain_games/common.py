from prompt import string


def play_game(description, generate_question_and_answer):
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(description)

    correct_answers_needed = 3
    correct_answers_given = 0

    while correct_answers_given < correct_answers_needed:
        question, correct_answer = generate_question_and_answer()
        print(f'Question: {question}')
        user_answer = string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers_given += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
