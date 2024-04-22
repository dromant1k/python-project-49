import random
from brain_games.brain_main import brain_main
import prompt


def brain_gcd():
    name = brain_main()
    print("Find the greatest common divisor of given numbers.")
    user_score = 0
    winscore = 3
    while user_score < winscore:
        a = random.randrange(1, 100)
        b = random.randrange(1, 100)
        print(f"Question: {a} {b}")
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        result = a + b
        answer = prompt.integer("You answer: ")
        if answer == result:
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
    brain_gcd()


if __name__ == '__main__':
    main()
