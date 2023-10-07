import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number: 
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Your guess is too low, guess again.')
        elif guess > random_number:
            print('Your guess is too high, guess again.') 
    
    print(f'Congratulations, you got it right! The random number is {random_number}')
        
guess(10)