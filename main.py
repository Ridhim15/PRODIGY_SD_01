print("Program to convert temperatur unit to Farenheit, Kelvin and Celsius")
while(True):
    print("Enter the temperature and select the unit")
    temp = float(input("Enter the temperature: "))
    unit = input("Enter the unit (C/F/K): ")
    match unit.upper():
        case "C":
            f = temp * 9/5 + 32
            k = temp + 273.15
            print(f"{temp}C is equal to {f}F and {k}K")
        case "F":
            c = (temp - 32) * 5/9
            k = c + 273.15
            print(f"{temp}F is equal to {c}C and {k}K")
        case "K":
            c = temp - 273.15
            f = c * 9/5 + 32
            print(f"{temp}K is equal to {c}C and {f}F")
        case _:
            print("Invalid unit")
    choice = input("Do you want to continue (y/n): ")
    if choice.lower() != "y":
        break
print("Program ended")
