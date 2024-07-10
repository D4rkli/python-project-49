import random


MAX_NUMBER = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(number1, number2):
    while number2:
        number1, number2 = number2, number1 % number2
    return number1


def generate_question_and_answer():
    num1 = random.randint(1, MAX_NUMBER)
    num2 = random.randint(1, MAX_NUMBER)
    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer
