def double(num: int):
    return num * 2


def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print(f"Double of {num} is equals to  {num_times_2}")

if __name__ == '__main__':
    main()