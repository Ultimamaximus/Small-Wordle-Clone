import random  # Import the random module for generating a random word

def generate_word():
    words = ["apple", "banana", "cherry", "orange", "pear", "grape", "kiwi", "mango", "papaya", "pineapple"]  # List of words to choose from
    return random.choice(words)  # Return a random word from the list

def get_guess():
    while True:
        guess = input("Guess a 5-letter word: ")  # Ask the user to input a guess
        if len(guess) != 5:
            print("Invalid guess. Please enter a 5-letter word.")  # If the guess is not 5 letters long, print an error message
        else:
            return guess  # If the guess is valid, return it

def evaluate_guess(guess, target_word, attempts):
    if guess == target_word:  # If the guess is correct
        print("Congratulations! You guessed the word!")
        return True  # Return True to indicate that the game has been won
    else:
        matched = 0  # Initialize a variable to count the number of matched letters
        matched_letters = []  # Initialize a list to store the matched letters
        for i in range(5):
            if guess[i] == target_word[i]:  # If the letters match
                matched += 1  # Increment the matched count
                matched_letters.append(guess[i])  # Add the matched letter to the list
        guesses_left = 5 - (attempts + 1)  # Calculate the number of guesses left
        if matched != 0:  # If there are matched letters
            print(f"Sorry, that's not the word. {matched} letter(s) match: {' '.join(matched_letters)}. You have {guesses_left} guess(es) left.")  # Print the matched letters and guesses left
        else:
            print(f"Sorry, that's not the word. None of the letters match. You have {guesses_left} guess(es) left.")  # Print the guesses left
        return False  # Return False to indicate that the game is not over yet

def play_game():
    target_word = generate_word()  # Generate a random word
    attempts = 0  # Initialize the number of attempts to 0
    while attempts < 5:  # Loop until the player has used up all their attempts
        guess = get_guess()  # Ask the player to guess a word
        if evaluate_guess(guess, target_word, attempts):  # Evaluate the guess
            break  # If the guess is correct, break out of the loop
        attempts += 1  # Increment the number of attempts
        guesses_left = 5 - attempts  # Calculate the number of guesses left
        print(f"You have {guesses_left} guess(es) left.")  # Print the guesses left
    else:
        print(f"Sorry, you didn't guess the word. The word was {target_word}.")  # If the player has used up all their attempts, print the correct word


play_game()