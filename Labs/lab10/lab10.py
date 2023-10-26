# managing Student Marks


class Student:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, standard, marks):
        self.students.append(
            {"Roll No": roll_no, "Name": name, "Class": standard, "Marks": marks}
        )
        print(f"Student Name {name} Succesfull added their Marks:)")
        print(self.students)

    def view_student(self):
        print("List of alll the Students")
        for i, data in enumerate(self.students, 1):
            print(f"{i}.")
            print(f"Name: {data['Name']}")
            print(f"Roll No: {data['Roll No']}")
            print(f"Class: {data['Class']}")
            print(f"Marks: {data['Marks']}")
            print()

    def search_student(self, search):
        search_status = False
        for data in self.students:
            if search == data["Name"] or search == data["Roll No"]:
                print(f"Name: {data['Name']}")
                print(f"Roll No: {data['Roll No']}")
                print(f"Class: {data['Class']}")
                print(f"Marks: {data['Marks']}")
                search_status = True
        if not search_status:
            print("Either This Student Does Not Exist OR Not add inyour database")


def main():
    student = Student()
    while True:
        print("-------Your Choices --------------")
        print("1. Teacher Pannel      2. Students Pannel")
        print("3. Exit")
        user_choice = int(input("Enter the user Choice: "))

        if user_choice == 1:
            print("You Are in Teacher Pannel!!")
            psw = input("Enter the Password To Access: ")

            if psw == "aman":
                while True:
                    print("-------Your Choices --------------")
                    print("1. Add Student       2. View all Student")
                    print("3. Exit")
                    user_input = int(input("Enter the user Choice: "))
                    if user_input == 1:
                        print("Adding the Pet in the Store!!")
                        name = input("Enter the Student Name: ")
                        roll = input("Enter The Student Roll Number: ")
                        standard = input("Enter the Class: ")
                        marks = input("Enter the Marks: ")
                        student.add_student(roll, name, standard, marks)
                    elif user_input == 2:
                        print("Now You Viewing All The Pets: ")
                        student.view_student()
                    elif user_input == 3:
                        print("Exitting....")
                        break

            else:
                print("OOPS your Password is Wrong!!")

        elif user_choice == 2:
            while True:
                print("This is The Customer Section of the Store!!")
                print("1. Serach By Name and Roll Number     2. Exit")

                user_input = int(input("Enter the user Choice: "))
                if user_input == 1:
                    change = (
                        input("Search By Which Method(Name / Roll No): ")
                        .strip()
                        .lower()
                    )
                    if change == "name":
                        student_data = input("Enter the Name: ")
                    elif change == "rollno":
                        student_data = input("Enter the Roll Number: ")
                    student.search_student(student_data)

                elif user_input == 2:
                    print("Exitting...")
                    break

        elif user_choice == 3:
            print("Exitting...")
            break


main()
