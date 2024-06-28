from brain_games.scripts.common import welcome_user, play_game
from brain_games.scripts.calc_game import generate_question_and_answer

def main():
    name = welcome_user()
    print('What is the result of the expression?')
    play_game(name, generate_question_and_answer)

if __name__ == '__main__':
    main()
