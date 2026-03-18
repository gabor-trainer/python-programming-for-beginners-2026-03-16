print("=== Temperature Converter ===")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print()

while True:
    choice = input("Select option (1 or 2): ")
    if choice == "1":
        while True:
            input_text = input("Enter temperature in Celsius: ")
            try:
                celsius = float(input_text)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        fahrenheit = celsius * 9 / 5 + 32
        print(f"{celsius}°C = {fahrenheit:.1f}°F")
        break
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit}°F = {celsius:.1f}°C")
        break
    else:
        print("Invalid option. Please enter 1 or 2.")
