# Here i make the first list til Zero to Nine
number = [
    "Zero",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
]

# Here i make the function called


def to_help_alice(number, user):
    str_user = str(user)
    new_value = ""
    for i in str_user:
        digit = int(i)
        new_value += number[digit]
    return new_value


user_input = int(input("Enter the Number: "))
result = to_help_alice(number, user_input)
print(f"{user_input}{result}")
