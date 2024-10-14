import random

# List of words to guess from
words = ['python', 'javascript', 'developer', 'coding', 'hangman']

def word_guessing_game():
    word_to_guess = random.choice(words)
    guessed_word = ['_'] * len(word_to_guess)
    attempts = 6  # Number of allowed attempts
    guessed_letters = []

    print("Welcome to the Word Guessing Game!")
    print("Try to guess the word. You have 6 attempts.")

    while attempts > 0:
        print(f"\nWord: {' '.join(guessed_word)}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[index] = guess
            if '_' not in guessed_word:
                print(f"\nCongratulations! You guessed the word: {word_to_guess}")
                break
        else:
            attempts -= 1
            print(f"Wrong guess! The letter '{guess}' is not in the word.")

    if attempts == 0:
        print(f"\nSorry, you've run out of attempts. The word was '{word_to_guess}'.")

# Run the game
if __name__ == "__main__":
    word_guessing_game()
