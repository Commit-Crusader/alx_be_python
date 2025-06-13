# Global Variable definition

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32)  * FAHRENHEIT_TO_CELCIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


temp = float(input(" Enter the temperature to convert: "))
unit = input(" Is this temperature in Celsius or in Fahrenheit? (C/F): ").strip().upper()

try:
    temperature = float(temp)

    if unit  == "F":
        converted = convert_to_celsius(fahrenheit)
        print(f"{temperature}°F is {converted}°C")
    elif unit == "C":
        converted = convert_to_fahrenheit(celsius)
        print(f"{temperatur}°C is {converted}°F")
    else:
        print(" Invalid unit, Enter 'C' for Celsius and 'F' for Fahrenheit.")
except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
