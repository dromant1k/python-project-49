from brain_games.brain_main import brain_main
from random import randint
import prompt
from math import sqrt


def brain_prime():
    name = brain_main()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    user_score = 0
    winscore = 3
    while user_score < winscore:
        number = randint(1, 100)
        simple = True
        i = 2
        print(f"Question: {number}")
        while i <= sqrt(number):
            if number % i == 0:
                simple = False
            i += 1
        answer = prompt.string("You answer: ")
        if simple == True and answer == 'yes':
            print("Correct!")
            user_score += 1
        if simple == False and answer == 'no':
            print("Correct!")
            user_score += 1
        if simple == True and answer != 'yes':
            print(f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'
Let's try again, {name}!""")
            user_score = 0
            break
        if simple == False and answer != 'no':
            print(f"""'{answer}' is wrong answer ;(. Correct answer was 'no'
Let's try again, {name}!""")
            user_score = 0
            break
        if user_score == 0:
            print(f"Let's try again, {name}")
        if user_score == 3:
            print(f"Congratulations, {name}!")


def main():
    brain_prime()


if __name__ == '__main__':
    main()