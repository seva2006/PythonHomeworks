import random

number_to_guess = random.randint(1, 100)
attempts = 10

for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}: Guess a number between 1 and 100: "))

    # Check the guess
    if guess > number_to_guess:
        print("Too high!")
    elif guess < number_to_guess:
        print("Too low!")
    else:
        print("You guessed it right!")
        break

else:
    print("You lost. Want to play again?")

play_again = input("Do you want to play again? (Y/y/YES/yes/ok): ").lower()
if play_again in ['y', 'yes', 'ok']:
    number_to_guess = random.randint(1, 100)
    attempts = 10
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Guess a number between 1 and 100: "))

        if guess > number_to_guess:
            print("Too high!")
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("You guessed it right!")
            break
else:
    print("Thanks for playing!")
