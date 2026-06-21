import random

# List of predefined words
words = ["python", "apple", "computer", "school", "mobile"]

# Select random word
word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

# Main game loop
while incorrect_guesses < max_attempts:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check input
    if guess in guessed_letters:
        print("You already guessed this letter!")
    
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")

    else:
        guessed_letters.append(guess)
        incorrect_guesses += 1
        print("Wrong guess!")

    # Check win condition
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 You won!")
        print("The word was:", word)
        break

else:
    print("\n😞 Game Over!")
    print("The word was:", word)