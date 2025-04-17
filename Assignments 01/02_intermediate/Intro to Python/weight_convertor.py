def main():
    print("Press 1 for Mercury")
    print("Press 2 for Venus")
    print("Press 3 for Mars")
    print("Press 4 for Jupiter")
    print("Press 5 for Saturn")
    print("Press 6 for Uranus")
    print("Press 7 for Neptune")

    earthling_weight = float(input('Enter your weight according to Earth in Kgs: '))
    which_planet = int(input("Enter your choice: "))

    if which_planet == 1:
        mercury_weight = earthling_weight * 0.376  # Calculate weight on Mercury
        mercury_weight = round(mercury_weight, 2)  # Round to 2 decimal places
        print(f"Your weight on Mercury is: {mercury_weight} kg")
        
    elif which_planet == 2:
        venus_weight = earthling_weight * 0.889  # Calculate weight on Venus
        venus_weight = round(venus_weight, 2)  # Round to 2 decimal places
        print(f"Your weight on Venus is: {venus_weight} kg")

    elif which_planet == 3:
        mars_weight = earthling_weight * 0.378  # Calculate weight on Mars
        mars_weight = round(mars_weight, 2)  # Round to 2 decimal places
        print(f"Your weight on Mars is: {mars_weight} kg")

    elif which_planet == 4:
        jupiter_weight = earthling_weight * 2.36  # Calculate weight on Jupiter
        jupiter_weight = round(jupiter_weight, 2)  # Round to 2 decimal places
        print(f"Your weight on Jupiter is: {jupiter_weight} kg")
    
    elif which_planet == 5:
        saturn_weight = earthling_weight * 1.081  # Calculate weight on Saturn
        saturn_weight = round(saturn_weight, 2)  # Round to 2 decimal places
        print(f"Your weight on Saturn is: {saturn_weight} kg")

    elif which_planet == 6:
        uranus_weight = earthling_weight * 0.815  # Calculate weight on Uranus
        uranus_weight = round(uranus_weight, 2)  # Round to 2 decimal places
        print(f"Your weight on Uranus is: {uranus_weight} kg")
    
    elif which_planet == 7:
        neptune_weight = earthling_weight * 1.14  # Calculate weight on Neptune
        neptune_weight = round(neptune_weight, 2)  # Round to 2 decimal places
        print(f"Your weight on Neptune is: {neptune_weight} kg")

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
