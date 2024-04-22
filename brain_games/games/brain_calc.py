import random
from brain_games.brain_main import brain_main
import prompt


def brain_calc():
    name = brain_main()
    print("What is the result of the expression?")
    user_score = 0
    winscore = 3
    while user_score < winscore:
        first_num = random.randint(1, 10)
        second_num = random.randint(1, 10)
        random_operator = random.choice(['+', '-', '*'])
        expression = f"{first_num} {random_operator} {second_num}"
        print(f"Question: {expression}")
        result = eval(expression)
        answer = prompt.string("You answer: ")
        if answer == str(result):
            print('Correct!')
            user_score += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  + f" Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
        if user_score == 3:
            print(f"Congratulations, {name}!")


def main():
    brain_calc()


if __name__ == '__main__':
    main()
