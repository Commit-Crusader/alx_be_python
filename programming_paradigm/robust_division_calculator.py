def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        
        divide = num / denom

    except ValueError:
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {divide}"
