import random

def main():
    # Pick a random number between 1 and 99
    number_to_guess = random.randint(1, 99)

    print("Guess the number I'm thinking of (between 1 and 99)...")

    user_guess = int(input("Your guess: "))

    # Keep looping until the correct guess
    while user_guess != number_to_guess:
        if user_guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")

        print()  # Clean spacing for the next prompt
        user_guess = int(input("Try again: "))

    print("Nice! You guessed it. The number was:", number_to_guess)

if __name__ == '__main__':
    main()
