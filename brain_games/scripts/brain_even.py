#!/usr/bin/env python3

import random
from brain_games.cli import welcome_user

def is_even(number):
    return number % 2 == 0

def generate_question_and_correct_answer():
    question = random.randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer

def main():
    user_name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    correct_answers_count = 0
    while correct_answers_count < 3:
        question, correct_answer = generate_question_and_correct_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        print("Correct!")
        correct_answers_count += 1
    print(f"Congratulations, {user_name}!")

if __name__ == "__main__":
    main()
