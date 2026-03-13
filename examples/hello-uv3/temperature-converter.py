# temperature.py - Celsius to Fahrenheit converter (extended)

temperatures_celsius = [0, 10, 20, 25, 30, 37, 100]

print("Celsius to Fahrenheit conversion table")
print("-" * 35)

for celsius in temperatures_celsius:
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"  {celsius:>6}°C  =  {fahrenheit:>6.1f}°F")
