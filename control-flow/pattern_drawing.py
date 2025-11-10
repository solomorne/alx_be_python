size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    for col in range(size):
        print("*", end="")
    print() 
    row += 1