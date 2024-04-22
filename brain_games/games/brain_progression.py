from brain_games.brain_main import brain_main
import random
from random import randint
import prompt


def brain_progression():
    name = brain_main()
    print("What number is missing in the progression?")
    user_score = 0
    winscore = 3
    while user_score < winscore:
        num_1 = randint(0, 85)
        num_2 = randint(99, 101)
        num_3 = randint(2, 3)
        list_of_ints = list(range(num_1, num_2, num_3))
        ten_random_numbers = list_of_ints[0:10]
        one_random_number = random.choice(ten_random_numbers)
        result = one_random_number
        index = ten_random_numbers.index(result)
        ten_random_numbers[index] = '..'
        print(f"Question: {ten_random_numbers}")
        answer = prompt.integer("You answer: ")
        if answer == result:
            print('Correct!')
            user_score += 1
        if answer != result:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
        if user_score == 3:
            print(f"Congratulations, {name}!")


def main():
    brain_progression()


if __name__ == '__main__':
    main()
