# First I create A class


class Stack:
    def __init__(self, item):
        self.item = item

    def add_stack(self, value):
        self.item.append(value)
        print(value + " This Value is Successfully Added")

    def remove_stack(self):
        print(self.item[-1] + " The Stack is Successfully Deleted")
        self.item.pop()

    def show_stack(self):
        for index, item in enumerate(self.item, 1):
            print(index, ": ", item)

    def is_empty(self):
        if len(self.item) == 0:
            print("Stack is Empty")
        else:
            print("Stack Has Some Value")


itemss = []
check_stack = Stack(itemss)
while True:
    try:
        print("1. Add Stack      2. Remove Stack")
        print("3. Check Empty Or Not      4. View Stack     5. Exit")
        user_input = int(input("Enter The Choices(1-5) : "))
    except ValueError:
        print("Make Choices in Integer Form")

    if user_input == 1:
        push = input("What Do You Want To add in a Stack: ")
        check_stack.add_stack(push)
    elif user_input == 2:
        check_stack.remove_stack()
    elif user_input == 3:
        check_stack.is_empty()
    elif user_input == 4:
        check_stack.show_stack()
    elif user_input == 5:
        print("Exitting...")
        break
