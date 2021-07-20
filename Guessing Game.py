# Joshua Snyder
# Random number guesser game
import random
import pyinputplus as pyip

# These values determine the range for the guess. Can be adjusted to fit the circumstance
lowest_guess = 1
highest_guess = 100

# Is in control of starting the program
def start():
    print("Welcome to the program")
    ready = str(input("Are you ready to play the number guesser game? Y/N ")).lower()
    if ready[0] == 'y':
        print("Okay lets get started with the game.")
        print("The computer will pick a random number between 1 and 100. Guess what that number is.")
        game()
    elif ready[0] == 'n':
        print("Okay come back when you are ready to play.")
    else:
        print("Sorry I did not understand that try again using Y/N")
        start()

# Main game loop
def game():
    computer_guess = int(random.randint(lowest_guess, highest_guess))
    guess = None
    count = 1
    while guess != computer_guess:
        guess = pyip.inputInt("Enter a number guess between 1 and 100: ")
        if guess > computer_guess:
            print("Too High, try again")
            count += 1
        elif guess < computer_guess:
            print("Too Low, try again")
            count += 1
        elif guess == computer_guess:
            print("Congratulations you guessed my number.")
            print(f"You guessed {count} times before finding the right number.")
            playAgain()

# Handles if the player wants play again or not
def playAgain():
    go_again = input("Do you want to play again? Y/N ").lower()
    if go_again[0] == 'y':
        game()
    elif go_again[0] == 'n':
        print("Okay, thanks for playing.")
    else:
        print("Sorry I don't understand. Try again.")
        playAgain()


start()