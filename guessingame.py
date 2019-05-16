import random
answer = random.randint(1,101)
print("Welcome to my number guessing game.\n")
guess  = input("Input a whole number between 1 and 100: ")
guess = int(guess)
guess_count = 1
out_of_guesses = False 

while (guess != answer) and not (out_of_guesses):
	if (guess_count < 5):

		if (guess > answer):
			guess = int(input("Too high! try again: "))
			guess_count += 1
		elif (guess < answer):
			guess = int(input("Too low! try again: "))
			guess_count += 1

	else:
		out_of_guesses = True

if (out_of_guesses == False):
	print("Congrats you did it, please go away now.")
elif(out_of_guesses == True):
	print("Too bad, you're out of guesses!")