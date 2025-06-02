while True:
    size = int(input("Enter the size of the pattern: "))
    if size.lower() == 'exit':
        break
    if size.isdigit():
        for _ in range(int(size)):
            print("*" * int(size))
    else:
        print("Invalid input. Enter a number")
