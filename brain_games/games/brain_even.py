from brain_games.brain_main import brain_main
import prompt
import random


def brain_even():
    name = brain_main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    user_score = 0
    winscore = 3
    while user_score < winscore:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = prompt.string("You answer: ")
        if number % 2 == 0 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        if number % 2 != 0 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
            user_score += 1
        if user_score == 3:
            print(f"Congratulations, {name}!")

def main():
    brain_even()

if __name__ == '__main__':
    main()
