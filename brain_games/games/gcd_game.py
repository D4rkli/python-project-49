import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer
