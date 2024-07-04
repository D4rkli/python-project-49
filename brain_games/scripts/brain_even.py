#!/usr/bin/env python3

from brain_games.common import play_game
from brain_games.games.even_game import generate_question_and_answer


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    play_game(description, generate_question_and_answer)


if __name__ == "__main__":
    main()
