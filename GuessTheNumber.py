import random as rand
import math

lower_limit = int(input("Give Lower Limit: "))
upper_limit = int(input("Give Upper Limit: "))
value = rand.randint(lower_limit, upper_limit)
x=math.log(upper_limit - lower_limit + 1, 2)
print("\n\t*You've only ",round(x)," chances to guess the integer*\n")
count = 0

while count < x:
	count += 1
	guess = int(input("Guess the number: "))
	if value == guess:
		print("Congrats you Guessed the Number in ",count, " try")
		break
	elif value > guess:
		print("You Guessed too SMALL!")
	elif value < guess:
		print("You Guessed too HIGH!")

if count >= math.log(upper_limit - lower_limit + 1, 2):
	print("\tBetter Luck Next time!")
	print("\nThe Number is ",value)