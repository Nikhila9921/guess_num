x = int(input())
import random
def guess(x):
    r_n=random.randint(1,x)
    guess = 0
    while guess != r_n:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < r_n:
            print('Sorry, guess agian.Too Low')
        elif guess > r_n:
            print('Sorry, guess again. too high')
    print(f'yay, congo. you have guess the number it is {r_n}')

guess(x)
