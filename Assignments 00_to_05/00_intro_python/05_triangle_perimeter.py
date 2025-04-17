def main():
    one_side_length = int(input('Enter the Length of first side: '))
    two_side_length = int(input('Enter the Length of second side: '))
    three_side_length = int(input('Enter the Length of third side: '))
    parameter = one_side_length + two_side_length + three_side_length

    print(f'The Paramter of your given length of triangle is equals to {parameter} ')


if __name__ == '__main__':
    main()