import random

# Dictionary of words with clues
WORD_CLUES = {
    "computer": "Electronic device for processing data",
    "coffee": "A popular beverage made from roasted beans",
    "car": "A vehicle with four wheels and an engine",
    "book": "A collection of written or printed pages bound together",
    "phone": "A device used for telecommunication",
    "music": "Sound organized in time",
    "friend": "A person whom one knows and with whom one has a bond of mutual affection",
    "dog": "A domesticated carnivorous mammal with a barking voice",
    "house": "A building for human habitation",
    "food": "Any nutritious substance that people or animals eat or drink",
    "money": "A medium of exchange in the form of coins and banknotes",
    "work": "Activity involving mental or physical effort done in order to achieve a purpose",
    "time": "The indefinite continued progress of existence",
    "family": "A group of one or more parents and their children living together as a unit",
    "school": "An institution for educating children",
    "love": "An intense feeling of deep affection",
    "health": "The state of being free from illness or injury",
    "game": "An activity engaged in for diversion or amusement"
}

# Function to print the current state of the hangman word
def print_word_state(word, guessed_letters):
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"Word: {display_word}")

# Function to print the current state of the hangman
def print_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
    ]
    print(stages[tries])

# Function to run the hangman game
def play_hangman():
    word, clue = random.choice(list(WORD_CLUES.items()))
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6  # Fixed number of max wrong guesses

    print("Welcome to Hangman!")
    print(f"Clue: {clue}")
    print_hangman(wrong_guesses)

    while wrong_guesses < max_wrong_guesses:
        print_word_state(word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You've guessed the word '{word}' correctly!")
                break
        else:
            wrong_guesses += 1
            guessed_letters.add(guess)
            print(f"Wrong guess. You have {max_wrong_guesses - wrong_guesses} attempts left.")
            print_hangman(wrong_guesses)

    if wrong_guesses == max_wrong_guesses:
        print_hangman(wrong_guesses)
        print(f"Game over! The word was '{word}'.")

# Entry point of the program
if __name__ == "__main__":
    play_hangman()
