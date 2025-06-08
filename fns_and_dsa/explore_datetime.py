from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and time: {formatted_date}")

def calculate_future_date():
    current_date = datetime.now()
    days_to_add = int(input("Enter a number of days: ")
    future_date = current_date + timedelta(days=days_to_add)
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date is: {formatted_date}")
