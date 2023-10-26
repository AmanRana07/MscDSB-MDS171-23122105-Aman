# crearte a petstore class where you have the details of pets available and their details
# The Class Will have methods
# Store a new Details
# Search For A PEt
# List all Pets

# Importing Your petstore Class , Create a petstoremain file , where you will implement a menu willl implement a menu driven program for admin  - who
# and  manage t willhe store and user who will see the pets and buy pets


# Let Begin the Code YOHOHOHOHO

import petModule


def main():
    pets = petModule.Petstore()
    while True:
        print("-------Your Choices --------------")
        print("1. Admin Pannel      2. Customer Section")
        print("3. Exit Order")
        user_choice = int(input("Enter the user Choice: "))

        if user_choice == 1:
            print("You Are in admin Pannel!!")
            psw = input("Enter the Password To Access: ")

            if psw == "aman":
                while True:
                    print("-------Your Choices --------------")
                    print("1. Add Pet       2. View Pet")
                    print("3. Exit")
                    user_input = int(input("Enter the user Choice: "))
                    if user_input == 1:
                        print("Adding the Pet in the Store!!")
                        pet_name = input("Enter the Pet Name: ")
                        age = int(input("Enter The Pet Age: "))
                        breed = input("Enter the Breed: ")
                        pets.add_pet(pet_name, age, breed)
                    elif user_input == 2:
                        print("Now You Viewing All The Pets: ")
                        pets.view_pet()
                    elif user_input == 3:
                        print("Exitting....")
                        break

            else:
                print("OOPS your Password is Wrong!!")

        if user_choice == 2:
            while True:
                print("This is The Customer Section of the Store!!")
                print("1. Search Pets       2. View Pets")
                print("3. Buy Pets        4. Exit")

                user_input = int(input("Enter the user Choice: "))
                if user_input == 1:
                    change = (
                        input("Search By Which Method(Name / Pet ID): ").strip().lower()
                    )
                    if change == "name":
                        pet_data = input("Enter the Pet Name: ")
                    elif change == "petid":
                        pet_data = input("Enter the Pet ID: ")
                    pets.search_pet(pet_data)

                elif user_input == 2:
                    print("Now You Viewing All The Pets: ")
                    pets.view_pet()

                elif user_input == 3:
                    change = (
                        input("SELL PET By Which Method(Name / Pet ID): ")
                        .strip()
                        .lower()
                    )
                    if change == "name":
                        pet_data = input("Enter the Pet Name: ")
                    elif change == "petid":
                        pet_data = input("Enter the Pet ID: ")
                    pets.sell_pet(pet_data)

                elif user_input == 4:
                    print("Exitting...")
                    break


main()
