# crearte a petstore class where you have the details of pets available and their details
# The Class Will have methods
# Store a new Details
# Search For A PEt
# List all Pets

# Importing Your petstore Class , Create a petstoremain file , where you will implement a menu willl implement a menu driven program for admin  - who
# and  manage t willhe store and user who will see the pets and buy pets


# Let Begin the Code YOHOHOHOHO

import random


class Petstore:
    def __init__(self):
        self.storing_pets = []

    def generate_pet_id(self):
        pet_id = ""
        for i in range(1, 6, 1):
            pet_id += str(random.randint(i, 10))
        return pet_id

    # this is the function for Adding the Pets
    def add_pet(self, pet_name, age, breed):
        pet_id = self.generate_pet_id()
        self.storing_pets.append(
            {
                "PetId": pet_id,
                "PetName": pet_name,
                "age": age,
                "breed": breed,
                "Sale": "Available",
            }
        )
        print(f"Your Pet Name: {pet_name} with Pet_id: {pet_id} is Successfully Added")
        print(self.storing_pets)

    # this is the function for Searching the Pets
    def search_pet(self, pet_data):
        for pets in self.storing_pets:
            if (pet_data == pets["PetId"] or pet_data == pets["PetName"]) and pets[
                "Sale"
            ] == "Available":
                print("--------------------------")
                print()
                print(f"Pet Id: {pets['PetId']}")
                print(f"Pet Name: {pets['PetName']}")
                print(f"Age: {pets['age']}")
                print(f"Breed: {pets['breed']}")
                print()
                print("--------------------------")
            else:
                print("Either This Pet Not Exist OR THe Pet Sold!!")

    # This functio is For Viewing all The Pets
    def view_pet(self):
        count = 0
        for pets in self.storing_pets:
            print()
            count += 1
            print("-----------------------------")
            print(f"{count}. Pet")
            print(f"Pet Id: {pets['PetId']}")
            print(f"Pet Name: {pets['PetName']}")
            print(f"Age: {pets['age']}")
            print(f"Breed: {pets['breed']}")
            print()
            print("-----------------------------")

    def sell_pet(self, pet_data):
        for pets in self.storing_pets:
            if pet_data == pets["PetId"] or pet_data == pets["PetName"]:
                pets["Sale"] = "Sold"
                print("You Successfully Sale the Pet!!")

            else:
                print("The Pet Not Exist!!")
