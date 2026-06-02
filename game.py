import random

print("--- Welcome to Rock, Paper, Scissors! ---")

options = ["rock", "paper", "scissors"]

# 1. Get User Input
user_choice = input("Choose rock, paper, or scissors: ").lower()

# 2. Computer makes a choice
computer_choice = random.choice(options)

print("\nYou chose: " + user_choice)
print("The computer chose: " + computer_choice)
print("-------------------------")

# 3. Determine the Winner
if user_choice == computer_choice:
    print("It's a tie!")

elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win! Rock smashes scissors.")
    else:
        print("You lose! Paper covers rock.")

elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win! Paper covers rock.")
    else:
        print("You lose! Scissors cuts paper.")

elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win! Scissors cuts paper.")
    else:
        print("You lose! Rock smashes scissors.")

else:
    print("Invalid input! Please check your spelling and try again.")