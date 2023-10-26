# First CREATE A LISTS
import random

item = [
    "Apple",
    "Banana",
    "oranges",
    "grapes",
    "Cherry",
    "Coconut",
    "Papaya",
    "Pomegranate",
    "Pineapple",
    "Sapota",
]
prices = [100, 200, 50, 300, 150, 400, 250, 130, 230, 99]
qty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# function to write a text in a csv

# For append the only 100 Item in a text File


def text_csv(file_name, item, price, qty):
    with open(file_name, "a") as csv:
        csv.write(f"{item},{price},{qty} \n")


def hun_item_loop():
    for i in range(100):
        random_for_item = random.randint(0, 9)
        random_for_price = random.randint(0, 9)
        random_for_qty = random.randint(0, 9)
        text_csv(
            "lab.txt",
            item[random_for_item],
            prices[random_for_price],
            qty[random_for_qty],
        )
    print("All the Items are Bing Added in the Csv File !!!")


# Now Open the File
def five_read_lins():
    print("You See the First 05 items of Price and Qty")
    with open("lab.txt", "r") as file:
        lines = file.readlines()

        data = lines[1:]

        for i, item in enumerate(data[:5]):
            split_data = item.strip().split(",")
            item = split_data[0]
            price = int(split_data[1])
            qty = int(split_data[2])
            total_cost = float(price * qty)
            print(f"Row {i+1}: {item}, Total Cost: {total_cost}")


def ten_read_lins():
    print("You See the Last 10 lince of Price and Qty")
    with open("lab.txt", "r") as file:
        lines = file.readlines()

        data = lines[1:]

        for i, item in enumerate(data[-10:]):
            split_data = item.strip().split(",")
            item = split_data[0]
            price = int(split_data[1])
            qty = int(split_data[2])
            total_cost = float(price * qty)
            print(f"Row {i+1}: {item}, Total Cost: {total_cost}")


def unique_items_names():
    with open("lab.txt", "r") as file:
        line = file.readlines()
        data = line[1:]

        unique_items = {}

        for i in data:
            split_data = i.strip().split(",")
            item = split_data[0]
            price = int(split_data[1])
            qty = int(split_data[2])
            total_cost = float(price * qty)
            if item in unique_items:
                unique_items[item] += total_cost

            else:
                unique_items[item] = total_cost
    print("\nTotal cost for each unique item:")
    for key, value in unique_items.items():
        print(f"{key}: {value}")


def find_min_max():
    item_prices = {}
    with open("lab.csv", "r") as csv_file:
        lines = csv_file.readlines()[1:]
        for line in lines:
            item_name, price, _ = line.strip().split(",")
            price = int(price)
            if item_name in item_prices:
                item_prices[item_name].append(price)
            else:
                item_prices[item_name] = [price]

    print("\nMinimum and Maximum Prices for each item:")
    for item_name, prices in item_prices.items():
        min_price = min(prices)
        max_price = max(prices)
        print(f"{item_name}: Min Price: {min_price}, Max Price: {max_price}")


def main():
    print("1. Create Lists for [Item, Quantity, Price]")
    print("2. See the first 5 and last 10 items")
    print("3. See the Unique list of Fruits")
    print("4. See the minimum & maximum price for each item sold")
    print("5. Exit")
    while True:
        try:
            user_choice = int(input("Enter Your Choice (1-5): "))

            if user_choice == 1:
                hun_item_loop()
            elif user_choice == 2:
                five_read_lins()
                print("----------------------------")
                ten_read_lins()
            elif user_choice == 3:
                unique_items_names()
            elif user_choice == 4:
                find_min_max()
            elif user_choice == 5:
                print("Exitting.....")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter The Value Integer")


main()
