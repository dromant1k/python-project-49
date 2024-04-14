#!/usr/bin/env python3

def greet(welcome):
    print(welcome)


def main():
    greet("Welcome to the Brain Games!")


if __name__ == '__main__':
    main()


from brain_games.cli import *


welcome_user()
