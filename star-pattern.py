# lets create a triangele


def right(rows):
    for i in range(1, rows + 1):
        print("*" * i)


def equilateral(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))


def reverseEquilateral(rows):
    for i in range(0, rows + 1):
        spaces = " " * (rows - (rows - i))
        star = "*" * (2 * (rows - i) - 1)
        print(spaces + star)


def triangles():
    user_range = int(input("Enter the Range for The Triangle: "))
    print("Lets Make a triangle ")
    print("1. Equilateral Triangle.        2. Reverse Triangle")
    print("3. Right Angle Triangle.        4. Exit")

    flag = 0
    while flag < 1:
        user_input = int(input("Enter the Number which tringle you want to see: "))
        if user_input == 1:
            equilateral(user_range)
        if user_input == 2:
            reverseEquilateral(user_range)
        if user_input == 3:
            right(user_range)
        if user_input == 4:
            print("Thanks For Using this Have a Good Day Biieeeee:}")
            flag = 1
            break


triangles()
