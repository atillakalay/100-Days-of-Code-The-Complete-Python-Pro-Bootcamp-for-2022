#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

chosen_word= random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
predictive_word = input("Please enter a word\n").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for word in chosen_word:
    if word == predictive_word:
        print("right")
    else:
        print("wrong")
