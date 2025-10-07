import sys

def show_menu():
    print("\nPython Learning Menu")
    print("1. Variables")
    print("2. Loops")
    print("3. Functions")
    print("4. Lists")
    print("5. Exit")

def explain_variables():
    print("\nVariables in Python store data. Example:")
    print("x = 5\nprint(x)")
    print("Output: 5")

def explain_loops():
    print("\nLoops repeat actions. Example:")
    print("for i in range(3):\n    print(i)")
    print("Output: 0\n1\n2")

def explain_functions():
    print("\nFunctions organize code. Example:")
    print("def greet(name):\n    print('Hello,', name)\ngreet('Alice')")
    print("Output: Hey, Alice")

def explain_lists():
    print("\nLists store multiple items. Example:")
    print("my_list = [1, 2, 3]\nprint(my_list)")
    print("Output: [1, 2, 3]")

def main():
    while True:
        show_menu()
        choice = input("Select a topic (1-5): ")
        if choice == '1':
            explain_variables()
        elif choice == '2':
            explain_loops()
        elif choice == '3':
            explain_functions()
        elif choice == '4':
            explain_lists()
        elif choice == '5':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
