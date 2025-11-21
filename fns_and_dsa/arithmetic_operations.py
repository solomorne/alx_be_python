def perform_operation(num1, num2, num3):
    
    if num3 == add:
        return num1 + num2
    elif num3 == subtract:
        return num1 - num2
    elif num3 == multiply:
        return num1 * num2
    elif num3 == divide:
        if num2 == 0:
            print("Undefined")
        else:
            return num1 / num2
    else:
        print("Not a Valid Number!!!")