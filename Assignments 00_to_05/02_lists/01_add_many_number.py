def calculate_numbers(numbers: list[int]) -> int:
    z = 0
    for number in numbers:
        z += number
    return z

def main():
    numbers_list = [5, 5, 5, 5]
    answer = calculate_numbers(numbers_list)
    print(answer)

if __name__ == "__main__":
    main()

    

