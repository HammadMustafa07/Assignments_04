def main():
    fruits = {'apple': 1.5, 'banana': 50, 'orange': 80, 'kiwi': 1, 'mango': 1.5, 'cheeku': 5}
    
    total_cost = 0
    for fruit in fruits:
        price = fruits[fruit]
        amount_bought = int(input(f"How many {fruit} do you want to buy?: "))
        total_cost += (price * amount_bought)
    
    print(f"Your total is  {str(total_cost)} $")



if __name__ == '__main__':
    main()