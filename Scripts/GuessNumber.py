#GUESS THE NUMBER GAME

import random
import time
import os

guesses = 0

print("Hello, what's your name?")
name = input('>>> ')
print("Hello " + name + ", Welcome!")

number = random.randint(1, 20)
print("Let's play a quick game!")
print("I'm thinking of a number between 1 and 20")

# A "FOR" LOOP, THAT LOOPS 6 TIMES
for guesses in range(6):
	print("Take a Guess!")
	guess = input('>>> ')
	guess =int(guess)
	
	if guess < number:
		print('Your number is too low.')
		
	if guess > number:
		print('Your guess is too high.')
		
	if guess == number:
		break
# FOR AFTER THE LOOP
if guess == number:
	guesses = str(guesses + 1)
	print('Good Job, ' + name + '! You guessed my number in ' + guesses + ' guesses')

else:
	number = str(number)
	print('Nope, the number I was thinking of was ' + number + '.')
	print('You lost bro. Sucks to suck')
	time.sleep(4)
	os.system('cls' if os.name == 'nt' else 'clear')				
