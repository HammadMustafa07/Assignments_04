def main():
  user_question = input('What do you want: ')
  if user_question == "Joke".lower():
    print("Here is a joke for you! Sophia is heading out\n to the grocery store. A programmer tells her: get a liter of milk,\n and if they have eggs, get 12. Sophia \n returns with 13 liters of milk. The programmer asks why and \n Sophia replies: 'because they had eggs'")
  else:
    print("Sorry I only tell jokes.")
if __name__ == '__main__':
    main()