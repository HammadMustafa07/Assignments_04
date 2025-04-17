def main():
    curr_value = 1
    while curr_value < 100:
        print(curr_value)
        curr_value = curr_value * 2
    print(curr_value)  # To print the final value that caused the loop to stop (>= 100)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
