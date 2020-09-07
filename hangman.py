import random

# function starts new game, opens text file and returns random word for game
def new_game():
	filehandle = open('words.txt','r')
	word = random.choice(filehandle.readlines())
	print("Welcome to Hangman, you have 6 lives.")
	filehandle.close()
	return word

# function checks if guess is good or bad.
def guess_letter(guess, word_tuple, user_display, lives):
	if len(guess) > 1 or len(guess) == 0 or guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
		print("Guess not valid, try again.")
	elif guess.lower() in word_tuple:
		for x in range(len(word_tuple)):
			if guess.lower() == word_tuple[x]:
				user_display[x] = guess.lower()
		print("Good guess!")
	else:
		print("Bad guess!")
		lives -= 1
		print("Guesses left: ",lives)
	return user_display, lives

# function checks if game is over either by guessing word or losing lives.
def game_over(user_display, lives):
	if "-" not in user_display:
		print("Congrats you solved the case")
		return True
	elif lives == 0:
		print()
		print("Game over, unlucky.")
		return True

# game function.
def game():
	lives = 6
	store_guess = []

	word = new_game()
	word_tuple = list(word)
	user_display = list("-"*(len(word)-1))
	print("The word is",user_display)

	while lives > 0:
		print()
		guess = input("Please guess a letter: ")
		if guess.lower() in store_guess:
			print("You guessed that already, try again.")
		else:
			store_guess.append(guess.lower())
			user_display, lives = guess_letter(guess,word_tuple,user_display,lives)
			print(user_display)
			if game_over(user_display,lives):
				print("The word was:",word)
				restart = input("Try again? press 'y' or press any key to quit:")
				if restart.lower() == 'y':
					game()
				else:
					print("Thanks for playing")

# call game function to start game.
game()
