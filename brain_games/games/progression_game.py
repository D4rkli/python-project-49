import random


PROGRESSION_LENGTH = 10
MAX_START_NUMBER = 10
MAX_STEP = 10
DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(start_number, step, length):
    progression = [start_number + step * i for i in range(length)]
    missing_index = random.randint(0, length - 1)
    correct_answer = str(progression[missing_index])
    progression[missing_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer


def generate_question_and_answer():
    start = random.randint(1, MAX_START_NUMBER)
    step = random.randint(1, MAX_STEP)
    return generate_progression(start, step, PROGRESSION_LENGTH)
