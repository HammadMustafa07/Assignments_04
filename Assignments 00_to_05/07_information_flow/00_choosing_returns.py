ADULT_AGE : int = 18 # U:S:A age 

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    
    return False

def main():
    age : str = int(input("Enter your age:  "))
    print(is_adult(age))
    

if __name__ == "__main__":
    main()