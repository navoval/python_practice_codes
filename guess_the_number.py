__author__ = 'changyunglin'

# ask an input to guess the number decide by the random function
import random

guesses_made = 0
name = raw_input("Hello! What's your name? ")
print 'Well, {0}, I am thinking a number between 1 and 20. You have 6 times to guess'.format(name)
number = random.randint(1, 20)
while guesses_made < 6:
    guess = int(raw_input('Take a guess: '))
    guesses_made += 1
    if guess < number:
        print 'Your guess is too low'
    if guess > number:
        print 'Your guess is too high'
    if guess == number:
        break

if guess == number:
    print 'Good job, {0}! You guessed my number {1} in {2} steps.'.format(name, number, guesses_made)
else:
    print 'Nope. The number I was thinking of was {0}.'.format(number)
