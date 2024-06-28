import random

def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])

    if operation == '+':
        question = f"{num1} + {num2}"
        answer = str(num1 + num2)
    elif operation == '-':
        question = f"{num1} - {num2}"
        answer = str(num1 - num2)
    else:  # operation == '*'
        question = f"{num1} * {num2}"
        answer = str(num1 * num2)

    return question, answer
