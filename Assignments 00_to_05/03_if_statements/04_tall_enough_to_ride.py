minimum_height = 50 # arbitrary units :)

def main():
    height = float(input("How tall are you? "))
    if (height >= minimum_height):
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, Inshallah next year!")


if __name__ == '__main__':
    main()