def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"{item} has been added")
            pass
        elif choice == '2':
            item = input("Enter an item to remove: ").strip()
            shopping_list.remove(item)
            print(f"{item} has been removed")
        else:
            print(f"{item} not found in the list")
            pass
        elif choice == '3':
            if shopping_list:
                print("\nYour Shopping List")
                for i, item in enumerate(shopping_list, 1)
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
