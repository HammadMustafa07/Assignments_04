import random 

roll_dice = 6

def main():
    die_1 = random.randint(1, roll_dice)
    die_2 = random.randint(1, roll_dice)
    total = die_1 + die_2

    print(f"First die {die_1}")
    print(f"Second die {die_2}")
    print(f"Total of two dices: {total}")


if __name__ == "__main__":
    main()
