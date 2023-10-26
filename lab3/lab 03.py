from termcolor import colored

number = [
    761,
    123,
    585,
    275,
    194,
    840,
    999,
    622,
    763,
    40,
    825,
    687,
    402,
    338,
    611,
    987,
    739,
    95,
    819,
    568,
    320,
    126,
    688,
    948,
    514,
    223,
    751,
    379,
    857,
    767,
    492,
    162,
    437,
    934,
    430,
    343,
    725,
    511,
    580,
    678,
    708,
    823,
    346,
    179,
    786,
    663,
    195,
    890,
    267,
    502,
    214,
    300,
    786,
    961,
    235,
    559,
    992,
    919,
    948,
    318,
    57,
    787,
    653,
    317,
    305,
    172,
    966,
    182,
    970,
    17,
    89,
    624,
    629,
    595,
    485,
    752,
    984,
    978,
    460,
    124,
    321,
    256,
    614,
    852,
    811,
    561,
    127,
    207,
    406,
    615,
    888,
    391,
    691,
    470,
    911,
    401,
    137,
    600,
    478,
    682,
]


def to_calculate_mean(list):
    count = 0
    sum = 0
    for i in list:
        sum += i
        count += 1
    return sum / count


def find_minimum(list):
    minimum = list[0]
    for i in list[1:]:
        if i < minimum:
            minimum = i
    return minimum


def find_maximum(list):
    maximum = list[0]
    for i in list[1:]:
        if i > maximum:
            maximum = i
    return maximum


def find_range(list):
    result = find_maximum(list) - find_minimum(list) / 2
    return result


def main():
    print("1. Mean          2.  min")
    print("3. max          4.  range     5. Exit")
    while True:
        try:
            user_choice = int(input("Enter Your Choice (1-5): "))

            if user_choice == 1:
                print(colored(to_calculate_mean(number), "yellow"))
            elif user_choice == 2:
                print(colored(find_minimum(number), "green"))
            elif user_choice == 3:
                print(colored(find_maximum(number), "blue"))
            elif user_choice == 4:
                print(colored(find_range(number), "magenta"))
            elif user_choice == 5:
                print(colored("Exiting...", "red", attrs=["reverse", "blink"]))
                break
            else:
                print(colored("Invalid choice.", "red", attrs=["reverse", "blink"]))
        except ValueError:
            print(colored("Enter The Value Integer", "red", attrs=["reverse", "blink"]))


if __name__ == "__main__":
    main()
