#!/usr/bin/env python3
from brain_games.common import play_game
from brain_games.games.calc_game import generate_question_and_answer


def main():
    description = 'What is the result of the expression?'
    play_game(description, generate_question_and_answer)


if __name__ == '__main__':
    main()
