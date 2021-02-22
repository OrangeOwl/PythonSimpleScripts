import time
import os
import sys

A = ["A", "a", "EH", "eh"]
B = ["B", "b", "BEE", "Bee", "bee", "bEE"]
X = ["exit", "Exit", "quit", "Quit", "leave", "Leave"]
Y = ["y", "Y", "yes", "YES", "Yes"] 
N = ["N", "n", "no", "NO", "No"]


def c_to_f():
	print("Input Temperature in Celsius")
	ans = input(">>> ")
	try:
    		temp = float(ans) * 1.8 + 32
    		print(temp)
    		print("Fahrenheit")
    		finished()
	except ValueError:
    		print ("This is not a number, try again")
    		time.sleep(2)
    		os.system('cls' if os.name == 'nt' else 'clear')
    		start()

def f_to_c():
	print("Input Temperature in Fahrenheit")
	ans = input(">>> ")
	try:
    		temp = (float(ans) - 32) / 1.8
    		print(temp)
    		print("Celsius")
    		finished()
	except ValueError:
    		print ("This is not a number, try again")
    		time.sleep(2)
    		os.system('cls' if os.name == 'nt' else 'clear')
    		start()

def start():
	print("Do you want to convert Celsius to Fahrenheit or Fahrenheit to Celsius? ")
	print("A:Celsius to Fahrenheit")
	print("B:Fahrenheit to Celsius")
	choice = input(">>> ")
	if choice in A:
		c_to_f()
	if choice in B:
		f_to_c()
	if choice in X:
		sys.exit('Goodbye!')	
	else:
		start()
		
def finished():
	print("Want to convert again?")
	choice = input(">>> ")
	if choice in Y:
		os.system('cls' if os.name == 'nt' else 'clear')
		start()
	if choice in N:
		sys.exit('Goodbye!')
	if choice in X:
		sys.exit('Goodbye!')
	else:
		print('Not a valid option')
		finished()						
start()
