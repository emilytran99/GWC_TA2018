while True:
	word = input("Type a word for someone to guess: ")
	word = word.lower()
	if(word.isalpha() == False):
		print("That's not a word!")
	else: 
		break

guesses = []
numfails = 0
maxfails = 7
wordToGuess = []
wordLen = len(word)

for letter in word:
	wordToGuess.append("_")

done = False

while not done: 
	print("----------------------------------------------")
	print("Here is what you've guessed correctly so far: ")
	print(wordToGuess)
	print("You have %d lives left" %(maxfails - numfails))
	print("These are the letters you've guessed so far: ")
	print(guesses)

	while True:
		guess = input("Guess a letter: ")

		if guess.isalpha() == False | len(guess) > 1:
			print("That's not a letter! Enter something else.")
		elif guess in guesses:
			print("You've already guessed that letter. Enter something else.")
		else:
			break

	if guess not in word:
		if len(guess) == 1 & guess.isalpha() == True:
			guesses.append(guess)
			print("That's not part of the word!")
			numfails += 1
		if numfails == 7:
			print("Sorry you're out of tries!")
			done = True
	else:
		for index in range(wordLen):
			if word[index] == guess:
				wordToGuess[index] = guess

		lettersLeft = 0
		for index in range(wordLen):
			if wordToGuess[index] == "_":
				lettersLeft += 1

		if lettersLeft == 0:
			print("You guessed the whole word!")
			done = True

print("Game over!")

