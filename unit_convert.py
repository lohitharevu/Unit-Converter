while True:
    print("\nUnit Conversion Menu:")
    print("1. Length Conversion")
    print("2. Weight Conversion")
    print("3. Temperature Conversion")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("\nLength Conversion:")
        print("1. Meters to Kilometers")
        print("2. Kilometers to Meters")
        print("3. Meters to Centimeters")
        print("4. Centimeters to Meters")
        
        sub_choice = input("Enter your choice: ")
        value = float(input("Enter the value to convert: "))
        
        if sub_choice == "1":
            print(f"{value} meters = {value / 1000} kilometers")
        elif sub_choice == "2":
            print(f"{value} kilometers = {value * 1000} meters")
        elif sub_choice == "3":
            print(f"{value} meters = {value * 100} centimeters")
        elif sub_choice == "4":
            print(f"{value} centimeters = {value / 100} meters")
        else:
            print("Invalid choice!")
    
    elif choice == "2":
        print("\nWeight Conversion:")
        print("1. Kilograms to Grams")
        print("2. Grams to Kilograms")
        print("3. Pounds to Kilograms")
        print("4. Kilograms to Pounds")
        
        sub_choice = input("Enter your choice: ")
        value = float(input("Enter the value to convert: "))
        
        if sub_choice == "1":
            print(f"{value} kg = {value * 1000} grams")
        elif sub_choice == "2":
            print(f"{value} grams = {value / 1000} kg")
        elif sub_choice == "3":
            print(f"{value} pounds = {value * 0.453592} kg")
        elif sub_choice == "4":
            print(f"{value} kg = {value / 0.453592} pounds")
        else:
            print("Invalid choice!")
    
    elif choice == "3":
        print("\nTemperature Conversion:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        
        sub_choice = input("Enter your choice: ")
        value = float(input("Enter the value to convert: "))
        
        if sub_choice == "1":
            print(f"{value}°C = {(value * 9/5) + 32}°F")
        elif sub_choice == "2":
            print(f"{value}°F = {(value - 32) * 5/9}°C")
        else:
            print("Invalid choice!")
    
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter 1-4.")