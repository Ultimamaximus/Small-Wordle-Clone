import random

def generate_word():
    words = ["apple", "banana", "cherry", "orange", "pear", "grape", "kiwi", "mango", "papaya", "pineapple"]
    return random.choice(words)

def get_guess():
    while True:
        guess = input("Guess a 5-letter word: ")
        if len(guess) != 5:
            print("Invalid guess. Please enter a 5-letter word.")
        else:
            return guess

def evaluate_guess(guess, target_word, attempts):
    if guess == target_word:
        print("Congratulations! You guessed the word!")
        return True
    else:
        matched = 0
        matched_letters = []
        for i in range(5):
            if guess[i] == target_word[i]:
                matched += 1
                matched_letters.append(guess[i])
        guesses_left = 5 - (attempts + 1)
        if matched != 0:
            print(f"Sorry, that's not the word. {matched} letters match: {' '.join(matched_letters)}. You have {guesses_left} guesses left.")
        else:
            print(f"Sorry, that's not the word. None of the letters match. You have {guesses_left} guesses left.")
        return False

def play_game():
    target_word = generate_word()
    attempts = 0
    while attempts < 5:
        guess = get_guess()
        if evaluate_guess(guess, target_word, attempts):
            break
        attempts += 1
        guesses_left = 5 - attempts
        print(f"You have {guesses_left} guesses left.")
    else:
        print(f"Sorry, you didn't guess the word. The word was {target_word}.")

play_game()
