def main():
    # Prompt the user to enter a year
    year = int(input('Please input a year: '))

    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If divisible by 4, check if it's also divisible by 100
        if year % 100 == 0:
            # If divisible by 100, it must also be divisible by 400 to be a leap year
            if year % 400 == 0:
                print("That's a leap year")
            else:
                print("That's not a leap year.")
        else:
            # Divisible by 4 but not by 100 — it's a leap year
            print("That's a leap year!")
    else:
        # Not divisible by 4 — not a leap year
        print("That's not a leap year.")


# Program execution starts here
if __name__ == '__main__':
    main()
