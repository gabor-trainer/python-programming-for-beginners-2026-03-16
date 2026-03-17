# temperature.py - Celsius to Fahrenheit converter (extended)

temperatures_celsius = [0, 10, 20, 25, 30, 37, 100, 200]

print("Celsius to Fahrenheit conversion table")
print("-" * 35)

for celsius in temperatures_celsius:
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"  {celsius:>12}°C  =  {fahrenheit:>16.1f}°F")
