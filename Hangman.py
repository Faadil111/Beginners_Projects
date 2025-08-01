import random

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
        ===''', '''
     +---+
     O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

words = ["tiger", "fauziyah", "fatih", "table", "artificial", "intelligence"]

# We are telling the computer to pick a random word
def get_word():
    secret_word = random.choice(words)
    return secret_word.lower()

# This function helps to check your missed letters display how much of the hangman has been completed as a result of your no. of tries
def displayBoard(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print("Missed Guesses:", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")
    print()

    blanks = "_" * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
        print (letter, end=" ")
    print()

# This function returns the letter the player entered and checks if you typed in a single letter
def getGuess(already_guessed):
    while True:
        print("Guess Letter: ")
        guess = input().lower()

        if len(guess) != 1:
            print("Please enter a single letter.")

        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")

        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER.")

        else:
            return guess

# This function returns true if the player wants to play again
def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")

print("Welcome to Hangman!")
missed_letters = ""
correct_letters = ""
secret_word = get_word()
game_over = False

while True:
    displayBoard(missed_letters, correct_letters, secret_word)

    #Let the player enter a letter
    guess = getGuess(missed_letters + correct_letters)
    if guess in secret_word:
        correct_letters += guess

        #Check if player has won
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print("Yes! The secret word is \"" + secret_word + "\"! You have won!")
            game_over = True
            break
    else :
       missed_letters += guess

       # Check if player has missed too many times and lost
       if len(missed_letters) == len(HANGMAN_PICS) - 1:
           displayBoard(missed_letters, correct_letters, secret_word)
           print("You have run out of guesses!\nAfter " + str(len(missed_letters)) + " missed guesses and " + str(len(correct_letters)) + " correct guesses, the word was \"" + secret_word + "\".")
           game_over = True

       #Ask the player if they want to play again when the game is already done
       if game_over:
           choice = input("Do you want to play again? (yes or no): ").lower()
           if  choice == "yes":
               playAgain()
               missed_letters = ""
               correct_letters = ""
               game_over = False
               secret_word = get_word()

           else:
               print("Thanks for playing!")
               break






