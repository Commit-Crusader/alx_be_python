# Global Variable definition

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


temp_str = float(input(" Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

try:
    temp = float(temp_str)

    if unit  == "F":
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted}°C")
    elif unit == "C":
        converted = convert_to_fahrenheit(celsius)
        print(f"{temp}°C is {converted}°F")
    else:
        print(" Invalid unit, Enter 'C' for Celsius and 'F' for Fahrenheit.")
except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
