from brain_games.common import play_game
from brain_games.games.progression_game import generate_question_and_answer


def main():
    description = 'What number is missing in the progression?'
    play_game(description, generate_question_and_answer)


if __name__ == '__main__':
    main()
