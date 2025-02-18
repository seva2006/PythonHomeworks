import random

player_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while player_score < 5 and computer_score < 5:
    player_choice = input("Enter rock, paper, or scissors: ").lower()

    if player_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "scissors" and computer_choice == "paper") or \
            (player_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Player score: {player_score} | Computer score: {computer_score}\n")

if player_score == 5:
    print("Congratulations! You win the game!")
else:
    print("Computer wins the game! Better luck next time.")
