import random 

num_sides = 6

def rolling_dice():
    die1 = random.randint(1, num_sides)
    die2 = random.randint(1, num_sides)
    print(f"Total of two dices: {die1 * die2}")
    

def main():
    rolling_dice()
    rolling_dice()
    rolling_dice()


if __name__ == '__main__':
    main()