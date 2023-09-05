def get_insight(file_name, second_file):
    with open(file_name + ".txt", "r") as order_file:
        print(f"Total Order Till Date: {order_file.read()}")
    with open(second_file + ".txt", "r") as price_file:
        print(f"Total Price Till Date: {price_file.read()}")


def to_order(name, price, phone_number, qty, total_guest, date, file_name):
    with open("total_order.txt", "r") as total_orders:
        total_order = int(total_orders.read())

    with open("total_price.txt", "r") as total_prices:
        total_price = float(total_prices.read())

    total_order += 1
    total_price_order = price * qty

    total_price += total_price_order

    with open("total_order.txt", "w") as order:
        order.write(str(total_order))

    with open("total_price.txt", "w") as total_prices:
        total_prices.write(str(total_price))

    with open(file_name + ".txt", "a+") as file:
        total_order = 0

        file.write(f"Total Order Till Date: {total_order}\n")
        file.write(f"Total Price from Orders to Date: {total_price}\n")
        file.write("---------------------------------\n")
        file.write(f"Name: {name}\n")
        file.write(f"Phone Number: {phone_number}\n")
        file.write(f"Food Price: {price}\n")
        file.write(f"Total qty: {qty}\n")
        file.write(f"Total Guest: {total_guest}\n")
        file.write(f"Date: {date}\n")
        file.write(f"Total price For This Order: {total_price_order}\n")
        file.write("---------------------------------\n")
        print("Your Order is Created Successfully")


def main():
    print("1. Create Order Data          2.  get Insight")
    print("3. exit")
    while True:
        try:
            user_choice = int(input("Enter Your Choice (1-2): "))

            if user_choice == 1:
                name = input("Customer Name: ")
                price = float(input("Food Price: "))
                phone_number = int(input("Customer Phone Number: "))
                qty = int(input("Quantity: "))
                guest = int(input("Total Guest: "))
                date = input("Date of the order: ")
                to_order(name, price, phone_number, qty, guest, date, "order")
            elif user_choice == 2:
                get_insight("total_order", "total_price")
            elif user_choice == 3:
                print("Exitting.....")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter The Value Integer")


if __name__ == "__main__":
    main()
