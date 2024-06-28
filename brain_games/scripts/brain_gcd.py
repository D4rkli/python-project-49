from brain_games.games.common import welcome_user, play_game
from brain_games.games.gcd_game import generate_question_and_answer


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    play_game(name, generate_question_and_answer)


if __name__ == '__main__':
    main()
