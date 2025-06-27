import random

def play_guessing_game():
#The code below specifies the smallest number and largest number which will serve as the range we will pick our random number from
    smallest_number = 0
    largest_number = 10
    secret_number = random.randint(smallest_number, largest_number)
    no_of_guesses = 0

    print("Welcome to the Number Guessing Game!")
    print(f"I have picked a number between {smallest_number} and {largest_number}. Lets see if you can guess it :).")

# The while loop below helps to start the game
    while no_of_guesses < 5:
       print("Enter '10' if you give up :) ")
       user_guess = int(input("Enter your guess: "))
       no_of_guesses += 1

#The code below checks whether the number you guess is the right one, if not it gives you a hint
       if user_guess == secret_number:
           print("Congratulations! You guessed the number!")

       elif user_guess > secret_number:
           print("Sorry, that's too high!")

       elif user_guess < secret_number:
           print("Sorry, that's too low!")

       elif user_guess < smallest_number or user_guess > largest_number:
           print("Sorry, that's out of range!")

       else:
           print("Invalid input! Try again!")
    print("Sorry man :(, You'll have to try again")




# This will serve as the opening screen of the game
opening_screen = input("""Welcome to Faadil's Guessing game ;)
Would you like to play ? (yes/no): """).lower()

if opening_screen == "yes":
    play_guessing_game()
else:
    print("Your choice :)")
