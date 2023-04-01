import random

# Define the list of words to choose from
WORDS = ['apple', 'banana', 'cherry', 'orange', 'pear']

# Choose a random word from the list
target_word = random.choice(WORDS)

# Define the number of guesses the player has
max_guesses = 6

# Define a list to keep track of the letters the player has guessed
guessed_letters = []

# Define a function to print the current state of the game
def print_game_state():
    print(' '.join([letter if letter in guessed_letters else '_' for letter in target_word]))

# Play the game
print('Welcome to Wordle! Guess the word in', max_guesses, 'tries or less.')
while max_guesses > 0:
    print('You have', max_guesses, 'guesses left.')
    print_game_state()
    guess = input('Guess a letter: ').lower()
    if guess in guessed_letters:
        print('You already guessed that letter.')
    else:
        guessed_letters.append(guess)
        if guess in target_word:
            print('Good guess!')
            if all([letter in guessed_letters for letter in target_word]):
                print_game_state()
                print('Congratulations, you win!')
                break
        else:
            print('Oops, that letter is not in the word.')
            max_guesses -= 1
else:
    print('Sorry, you lose. The word was', target_word)