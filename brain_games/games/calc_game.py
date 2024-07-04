import random


def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2


def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(['+', '-', '*'])
    question = f"{num1} {op} {num2}"
    correct_answer = str(calculate(num1, num2, op))
    return question, correct_answer
