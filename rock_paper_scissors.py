# importing the random and wasabi libraries
import random
from wasabi import Printer

# assigned an instance of the Printer class to a variable
msg = Printer()


# defined a function for the game logic
def game():

    while True:
        print()  # Add a blank line
        msg.text("ROCK PAPER SCISSORS CHOICES", color="pink")
        msg.text("Please select one of the following options:")
        msg.text("------------------------", color="cyan")
        msg.text("       1. Rock", color="yellow")
        msg.text("       2. Paper", color="yellow")
        msg.text("       3. Scissors", color="yellow")
        msg.text("------------------------", color="cyan")
        choice = input("Enter here:")

        # created a list with the choices
        list_choice = ["Rock", "Paper", "Scissors"]

        # used the choice function from the random library so that the and assigned the random choice to a variable
        comp_choice = random.choice(list_choice)

        # if the choice is equal to rock
        if choice == "1":

            # Check the user's choice against the computer's choice and determine the result
            msg.text(f"Computer choose {comp_choice}", color="blue")

            if comp_choice == "Paper":
                msg.text("YOU LOSE", color="red")  # Player loses when computer chooses Paper
                break

            elif comp_choice == "Scissors":
                msg.text("YOU WIN ", color="green")  # Player wins when computer chooses Scissors
                break

            elif comp_choice == "Rock":
                msg.text("IT'S A TIE", color="yellow")  # It's a tie when computer also chooses Rock
                break

        # if the choice is equal to paper
        elif choice == "2":

            # Check the user's choice against the computer's choice and determine the result
            msg.text(f"Computer choose {comp_choice}", color="blue")

            if comp_choice == "Rock":
                msg.text("YOU WIN", color="green")  # Player wins when computer chooses Rock
                break

            elif comp_choice == "Scissors":
                msg.text("YOU LOSE", color="red")  # Player loses when computer chooses Scissors
                break

            elif comp_choice == "Paper":
                msg.text("IT'S A TIE", color="yellow")  # It's a tie when computer also chooses Paper
                break

        # if the choice is equal to scissors
        elif choice == "3":

            # Check the user's choice against the computer's choice and determine the result
            msg.text(f"Computer choose {comp_choice}", color="blue")

            if comp_choice == "Rock":
                msg.text("YOU LOSE", color="red")  # Player loses when computer chooses Rock
                break

            elif comp_choice == "Paper":
                msg.text("YOU WIN", color="green")  # Player wins when computer chooses Paper
                break

            elif comp_choice == "Scissors":
                msg.text("IT'S A TIE", color="yellow")  # It's a tie when computer also chooses Scissors
                break

        # used an else statement for when the user inputs an invalid choice
        else:
            # the msg.warn() to display a warning message when the user input an invalid choice
            msg.warn("Invalid choice. Please try again.\n")


# defined a function for the "play again" option
def play_again():
    while True:

        print()  # Add a blank line
        # provided menu for weather the user wants to play again or exit the program
        msg.text("ROCK PAPER SCISSORS MENU", color="pink")
        msg.text("Please select one of the following options:")
        msg.text("------------------------", color="cyan")
        msg.text("       1. Play again?", color="yellow")
        msg.text("       2. Exit", color="yellow")
        msg.text("------------------------", color="cyan")

        # asked the user tp enter there option here
        play = input("Enter here:")

        if play == "1":
            game()   # called the game function
            print()  # Added a blank line

        # used an elif statement for when the user selects to exit
        elif play == "2":

            # the msg.text() to display a goodbye message for the user selects to exit the program
            msg.text("Thank you for playing Rock Paper Scissors! Goodbye!", color="yellow")

            # used the exit function to exit the code
            exit()
        else:

            # the msg.warn() to display a warning message when the user input an invalid choice
            msg.warn("\nInvalid choice. Please try again.\n")
            print()  # Added a blank line


# defined a function for the main menu
def menu():

    while True:
        print()  # Add a blank line
        msg.text("ROCK PAPER SCISSORS MENU", color="pink")
        msg.text("------------------------", color="cyan")
        msg.text("Please select one of the following options:")
        msg.text("       1. Play", color="yellow")
        msg.text("       2. Exit", color="yellow")
        msg.text("------------------------", color="cyan")

        # asked the user to input there choice here
        play_choice = input("\nEnter here:\n")

        # used an if statement for when the user selects to play
        if play_choice == "1":
            game()   # called the game
            play_again()   # called the play_again function

        # used an elif statement for when the user selects to exit
        elif play_choice == "2":

            # the msg.text() to display a goodbye message for the user selects to exit the program
            msg.text("Thank you for playing Rock Paper Scissors! Goodbye!", color="yellow")

            # used the exit function to exit the code
            exit()

        else:
            # the msg.warn() to display a warning message when the user input an invalid choice
            msg.warn("\nInvalid choice. Please try again.\n")


# called the menu function
menu()
