def main():
    name : str = input("What's your name? ")
    print(greet(name))


def greet(name):
    return f"Greetings {name} !"
	
if __name__ == '__main__':
    main()
