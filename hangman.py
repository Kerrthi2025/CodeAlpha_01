import random

# List of words to choose from
words = ['python', 'hangman', 'programming', 'oii', 'Keerthi', 'Praveen']

def get_random_word(word_list):
    """Select a random word from the word list."""
    return random.choice(word_list)

def display_current_progress(word, guessed_letters):
    """Display the current progress of the guessed word."""
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print('Current progress:', display_word)
    return display_word

def play_hangman():
    """Main function to play the Hangman game."""
    word = get_random_word(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Limit on the number of incorrect guesses

    print("Welcome to Hangman Game!")
    print(f"The word has {len(word)} letters.")
    display_current_progress(word, guessed_letters)

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Fantastic!!Good guess! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f" Oops.....Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        current_progress = display_current_progress(word, guessed_letters)
        
        if '_' not in current_progress:
            print("Congrats! The guess is correct.")
            break
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()
