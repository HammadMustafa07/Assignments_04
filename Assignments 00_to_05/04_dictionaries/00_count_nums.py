# Dictionary to store number counts
number_count = {}

# Ask user how many numbers they want to enter
n = int(input("How many numbers do you want to enter? "))

# Take inputs and count them
for _ in range(n):
    num = int(input("Enter a number: "))
    if num in number_count:
        number_count[num] += 1
    else:
        number_count[num] = 1

# Print the results
print("\nResults:")
for num, count in number_count.items():
    print(f"{num} was {count} times")
