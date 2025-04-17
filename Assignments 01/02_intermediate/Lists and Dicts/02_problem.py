# Accessing Elements:

# diff_list = ["hammad", "asad", 1, 7, True]

# def main():
#     list_index = int(input("Enter the index: ")) 
#     if 0 <= list_index < len(diff_list):  
#         print(diff_list[list_index])
#     else:
#         print("Invalid index!")

# if __name__ == "__main__":
#     main()


# Modifying Elements:

# def main():
#     diff_list = ["hammad", "asad", 1, 7, True]


#     desired_index = int(input("Enter your index: "))
#     desired_Element = (input("Enter your Element: "))

#     diff_list[desired_index] = desired_Element

#     print(diff_list)
# if __name__ == "__main__":
#     main()

# Slicing the List:

# diff_list = ["hammad", "asad", 1, 7, True]
# new_list = []

# def main(my_list, start, end):
#     if start < 0 or end > len(my_list) or start >= end:
#         print("Invalid Index!")
#         return

#     for i in range(start, end):
#         new_list.append(my_list[i])

# if __name__ == "__main__":
#     main(diff_list, 0, 5)
#     print(new_list)

# Game Interaction:

# diff_list = ["hammad", "asad", 1, 7, True]

# def main():
#     print("Welcome to the List Game!")
#     print("Choose an operation:")
#     print("1. Access")
#     print("2. Modify")
#     print("3. Slice")

#     choice = input("Enter your choice (1/2/3): ")

#     if choice == "1":
#         index = int(input("Enter the index to access: "))
#         if 0 <= index < len(diff_list):
#             print(f"Value at index {index} is: {diff_list[index]}")
#         else:
#             print("Invalid index!")

#     elif choice == "2":
#         index = int(input("Enter the index to modify: "))
#         if 0 <= index < len(diff_list):
#             new_value = input("Enter the new value (as string): ")
#             diff_list[index] = new_value  # Storing as a string directly
#             print(f"Updated list: {diff_list}")
#         else:
#             print("Invalid index!")

#     elif choice == "3":
#         start = int(input("Enter start index: "))
#         end = int(input("Enter end index: "))
#         if 0 <= start < len(diff_list) and 0 < end <= len(diff_list) and start < end:
#             new_list = []
#             for i in range(start, end):
#                 new_list.append(diff_list[i])
#             print(f"Sliced list: {new_list}")
#         else:
#             print("Invalid slice range!")

#     else:
#         print("Invalid choice!")

#     print(f"Final list state: {diff_list}")

# if __name__ == "__main__":
#     main()




