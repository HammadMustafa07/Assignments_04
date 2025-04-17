import random



def high_low_game(rounds=5):
    score = 0

    print("Welcome to the High-Low Game!")
    print(f"You will play {rounds} rounds against the computer.\n")

    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}:")

        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is: {your_number}")
        guess = input("Do you think your number is (h)igher or (l)ower than the computer's number? ").lower()

        # Validate guess
        while guess not in ['h', 'l']:
            guess = input("Invalid input. Please enter 'h' for higher or 'l' for lower: ").lower()

        if (guess == 'h' and your_number > computer_number) or (guess == 'l' and your_number < computer_number):
            print("Correct guess! You get a point.")
            score += 1
        else:
            print("Wrong guess.")

        print(f"The computer's number was: {computer_number}")
        print(f"Your current score: {score}\n")

    print("Game Over!")
    print(f"Your final score is: {score}/{rounds}")

# Start the game


if __name__ == "__main__":
  high_low_game()