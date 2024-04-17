import random
from random import randint
from brain_games.brain_main import brain_main
import prompt
import operator


name = brain_main()


def brain_calc():
    print("What is the result of the expression?")
    index = 0
    winscore = 3
    while index < winscore:
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
            index = index + 1
        if answer != result:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{result}'
Let's try again, {name}!""")
            index = 0
    print(f"Congratulations, {name}!")


def main():
    brain_calc()


if __name__ == '__main__':
    main()
