import random
n=int(input("Enter a number"))
def guess(n):
	random_number = random.randint(1,n)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Guess a number between 1 and {n}: '))
		if guess < random_number:
			print("sorry ,you entered a number less than tye correct number.Guess Again!")
		elif guess > random_number:
			print("sorry ,you entered a number greater  than tye correct number.Guess Again!")
	print(f' Congrats,You have guessed the number {random_number } correctly')
guess(n)

			