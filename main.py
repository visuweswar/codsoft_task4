import random

# Define the possible moves
moves = ["rock", "paper", "scissors"]

# Take user input
user_action = input("Enter a choice (rock, paper, scissors): ")

# Make the computer choose
computer_action = random.choice(moves)

# Determine the winner
if user_action == computer_action:
    print(f"Both players chose {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cut paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cut paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")

# Play again?
play_again = input("Do you want to play again? (yes/no): ")
if play_again.lower() == "yes":
    print("\n")
    # Recurse to play another round
    exec(open(__file__).read())
else:
    print("Thanks for playing! Have a great day!")