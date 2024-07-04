import random


PROGRESSION_LENGTH = 10
MAX_START_NUMBER = 10
MAX_STEP = 10


def generate_progression(start, step, length):
    return [start + step * i for i in range(length)]


def generate_question_and_answer():
    start = random.randint(1, MAX_START_NUMBER)
    step = random.randint(1, MAX_STEP)
    length = PROGRESSION_LENGTH
    progression = generate_progression(start, step, length)

    missing_index = random.randint(0, length - 1)
    correct_answer = str(progression[missing_index])
    progression[missing_index] = '..'

    question = ' '.join(map(str, progression))
    return question, correct_answer
