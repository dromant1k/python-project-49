import prompt


def brain_main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


if __name__ == '__main__':
    brain_main()
