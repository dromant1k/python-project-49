from brain_games.brain_main import brain_main
from random import randint
import prompt


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def brain_prime():
    name = brain_main()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    user_score = 0
    winscore = 3
    while user_score < winscore:
        number = randint(1, 100)
        is_simple = is_prime(number)
        print(f"Question: {number}")
        answer = prompt.string("You answer: ")
        if (is_simple and answer == 'yes') \
            or (not is_simple and answer == 'no'):
            print("Correct!")
            user_score += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  + f" Correct answer was '{'yes' if is_simple else 'no'}'.")
            print(f"Let's try again, {name}!")
            break

        if user_score == 3:
            print(f"Congratulations, {name}!")


def main():
    brain_prime()


if __name__ == '__main__':
    main()
