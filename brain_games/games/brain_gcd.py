from random import randrange
from brain_games.brain_main import brain_main
import prompt


def brain_gcd():
    name = brain_main()
    print("Find the greatest common divisior of given numbers.")
    index = 0
    winscore = 3
    while index < winscore:
        a = randrange(1, 100)
        b = randrange(1, 100)
        print(f"Question: {a} {b}")
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        result = a + b
        answer = prompt.integer("You answer: ")
        if answer == result:
            print('Correct!')
            index = index + 1
        if answer != result:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{result}'
Let's try again, {name}!""")
            index = 0
    print(f"Congratulations, {name}!")


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
