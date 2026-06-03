import random

print("--- Welcome to Rock, Paper, Scissors: Best of 3! ---")

options = ["rock", "paper", "scissors"]

# Initialize the scores at 0
user_score = 0
computer_score = 0

# The loop keeps going as long as BOTH scores are less than 3
while user_score < 3 and computer_score < 3:
    print(f"\nScore -> You: {user_score} | Computer: {computer_score}")
    
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    # Check for invalid input before making the computer choose
    if user_choice not in options:
        print("Invalid input! Please check your spelling.")
        continue  # This skips the rest of the loop and restarts the round
        
    computer_choice = random.choice(options)
    print(f"The computer chose: {computer_choice}")
    print("-------------------------")

    # Determine the round winner
    if user_choice == computer_choice:
        print("It's a tie for this round!")

    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win this round!")
            user_score = user_score + 1
        else:
            print("Computer wins this round!")
            computer_score = computer_score + 1

    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win this round!")
            user_score = user_score + 1
        else:
            print("Computer wins this round!")
            computer_score = computer_score + 1

    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win this round!")
            user_score = user_score + 1
        else:
            print("Computer wins this round!")
            computer_score = computer_score + 1

# The loop has ended, which means someone reached 3 points!
print("\n=========================")
print("       FINAL GAME OVER   ")
print("=========================")
print(f"Final Score -> You: {user_score} | Computer: {computer_score}")

if user_score == 3:
    print("Congratulations! You won the tournament! 🎉")
else:
    print("The computer won the tournament. Better luck next time! 🤖")