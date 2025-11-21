# Create an empty list
shopping_list =[]

# Define a function to add items to shopping list
def add_item(item):
    shopping_list.append(item)
    print(f"{item} added to list")

# Define a function to remove items from shopping list
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from list")
    else:
        print(f"{item} not found in shopping list")

# Define a function to display items in shopping list
def display_list():
    if shopping_list:
        for item in shopping_list:
            print(f"{item}")
    else:
        print("Your shopping list is empty")

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select a number (1-4): ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter an item to add: ")
            add_item(item)
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter an item to remove: ")
            remove_item(item)
        elif choice == '3':
            # Display the shopping list
            display_list
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()