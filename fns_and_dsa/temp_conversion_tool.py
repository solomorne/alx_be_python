# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Takes a temperature in Fahrenheit and returns the temperature converted to Celsius.
    Uses the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    Formula: (F - 32) * (5/9)
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Takes a temperature in Celsius and returns the temperature converted to Fahrenheit.
    Uses the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    Formula: (C * 9/5) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # User Interaction: Get temperature input
        temp_input = input("Enter the temperature to convert: ")
        
        # Input validation: Check if input is numeric
        try:
            temperature = float(temp_input)
        except ValueError:
            # Raising the specific error message requested
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        # User Interaction: Get unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Logic to call appropriate function based on unit
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
            
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
            
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        # Catch the error raised above and print it cleanly for the user
        print(e)

if __name__ == "__main__":
    main()