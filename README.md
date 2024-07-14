# CodeAlpha_01
This Python program implements a simple text-based Hangman game. Here's an explanation of how it works:

Word Selection: The game starts by randomly selecting a word from a predefined list of words. This is done using get_random_word function.

Displaying Progress: The function display_current_progress chooses the word and the set of guessed letters as input, then constructs and prints a string showing the current state of the word. Correctly guessed letters are displayed in their correct positions, while unguessed letters are represented by underscores.

Game Loop: The play_hangman function contains the main game loop:

It initializes the game with the selected word, an empty set of guessed letters, and a counter for incorrect guesses.
The game welcomes the player and shows the number of letters in the word.
The loop continues to prompt the player to guess a letter until they either guess the word correctly or exceed the maximum number of incorrect guesses (set to 6).
For each guess, the program checks if the input is valid (a single alphabetic character) and whether the letter has already been guessed.
If the guess is correct, the letter is added to the set of guessed letters, and the current progress of the word is displayed.
If the guess is incorrect, the number of incorrect guesses is incremented, and the player is informed of how many guesses they have left.
If the player correctly guesses the word before running out of guesses, they win the game. Otherwise, they lose, and the correct word is revealed.
