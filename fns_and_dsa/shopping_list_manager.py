def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # start with an empty list

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(item, "has been added to your shopping list.")

        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(item, "has been removed from your shopping list.")
            else:
                print(item, "is not in your shopping list.")

        elif choice == '3':
            # Display the shopping list
            if len(shopping_list) == 0:
                print("Your shopping list is empty.")
            else:
                print("Your Shopping List:")
                for i in range(len(shopping_list)):
                    print(i + 1, "-", shopping_list[i])

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
