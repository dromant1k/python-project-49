import prompt
import random


def greet():
    print("Welcome to the Brain Games!")



def brain_even():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    winscore = 3
    while index < winscore:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = prompt.staring("You answer: ")
        if number % 2 == 0 and answer != 'yes':
            print(f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}""")
            index = 0
        elif number % 2 != 0 and answer != 'no':
            print(f"""'{answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}""")
            index = 0
        else:
            print("Correct!")
            index += 1
    print(f"Congratulations, {name}!")


def main()"
    greet()
    brain_even()



if __name__ == '__main__':
    main()
