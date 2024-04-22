import random
from random import randint
from brain_games.brain_main import brain_main
import prompt
import operator


def brain_calc():
    name = brain_main()
    print("What is the result of the expression?")
    user_score = 0
    winscore = 3
    while user_score < winscore:
        first_number = randint(1, 10)
        second_number = randint(1, 10)
        operator = ['+', '-', '*']
        random_operator = random.choice(operator)
        expression = f"{first_number} {random_operator} {second_number}"
        print(f"Question: {expression}")
        if '+' == random_operator:
            result = str(first_number + second_number)
        if '-' == random_operator:
            result = str(first_number - second_number)
        if '*' == random_operator:
            result = str(first_number * second_number)
        answer = prompt.string("You answer: ")
        if answer == result:
            print('Correct!')
            user_score += 1
        if answer != result:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{result}'
Let's try again, {name}!""")
            user_score = 0
            break
        if user_score == 0:
            print(f"Let's try again, {name}")
        if user_score == 3:
            print(f"Congratulations, {name}!")


def main():
    brain_calc()


if __name__ == '__main__':
    main()
