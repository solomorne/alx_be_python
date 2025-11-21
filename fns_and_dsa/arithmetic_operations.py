# Perform basic arithmetic function
def perform_operation(num1, num2, operation):

# Using the conditional statement to add, subtract, multiply and divide
    if operation == add:
        return num1 + num2
    elif operation == subtract:
        return num1 - num2
    elif operation == multiply:
        return num1 * num2
    elif operation == divide:
        if num2 == 0:
            print("Undefined")
        else:
            return num1 / num2
    else:
        print("Not a Valid Number!!!")