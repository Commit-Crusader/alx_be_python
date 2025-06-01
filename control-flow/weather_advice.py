"""
Create a Python script named weather_advice.py.
This script will ask the user about the current weather conditons and 
provide clothing recommendations based on the input.

input: we are going to take a string as input and store that in weather
weather conditions is going to be sunny, rainy or cold.
"""
weather = input("What's the weather like today? (sunny/rainy/cold):.").lower()
if weather == 'sunny':
    print("Wear a t-shirt and sunglasses.")
elif weather == 'rainy':
    print("Don't forget your umbrella and a raincoat.")
elif weather == 'cold':
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations fort this weather.")
