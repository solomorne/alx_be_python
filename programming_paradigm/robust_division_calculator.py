def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError as e:
        return f"Error: Cannot divide by zero. {e}"
    except ValueError as e:
        return f"Error: Please enter numeric values only. {e}"
