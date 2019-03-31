import random


def change():

    chances = 10

    x = random.randint(0,100)

    print("Guess the number: ")

    y = int(input())
    while y != x and chances != 0:
        if y > x:
            print('Too high')
            chances = chances - 1
        elif y < x:
            print('Too low')
            chances = chances - 1
        y = int(input())

    if chances == 0:
        print('Chances are over chief :(\n The answer was: ', x)
    else:
        print('you got it chief! The number was:', x)
    play_again = input('\nWanna play again? (Yes/No) ')
    if play_again == 'Yes':
        change()


change()
