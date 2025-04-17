c = 299792458 # speed of light in m/s

def main():
    m =  float(input("Enter your weight in Kgs: "))
    e = m * (c ** 2)
    print(f"{e} joules of energy..")



if __name__ == '__main__':
    main()