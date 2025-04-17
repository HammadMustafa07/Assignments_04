AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print(f"Enter the following Affirmation {AFFIRMATION}")

    user_input = input()
    while(user_input != AFFIRMATION):
        print("That was not the affirmation.")


        print(f"Enter the following Affirmation {AFFIRMATION}")
        user_input = input()



if __name__ == "__main__":
    main()