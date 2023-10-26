import csv


class expenseTracker:
    def __init__(self, csv_filename):
        self.expenseDict = {
            "income": [],
            "expense": [],
        }
        self.csv_filename = csv_filename

        # Create the CSV file and write the header if it doesn't exist
        with open(self.csv_filename, mode="a+", newline="") as file:
            writer = csv.writer(file)
            # Check if the file is empty and write the header if needed
            if file.tell() == 0:
                writer.writerow(["Amount", "Category", "Date", "Details", "Type"])

    def store_transactions(self, type, amt, category, date, details):
        trans = {
            "Amount": amt,
            "Category": category,
            "Date": date,
            "Details": details,
        }
        if type == "income":
            self.expenseDict["income"].append(trans)
            transaction_type = "Income"
        else:
            self.expenseDict["expense"].append(trans)
            transaction_type = "Expense"

        # Add the transaction to the CSV file with the transaction type
        self.add_transaction_to_csv(amt, category, date, details, transaction_type)

    def view_transactions(self):
        print("Your Income:")
        for item in self.expenseDict["income"]:
            print(item)
        print("Your Expenses:")
        for item in self.expenseDict["expense"]:
            print(item)

    def calculate_transactions(self):
        total_income = sum(item["Amount"] for item in self.expenseDict["income"])
        total_expense = sum(item["Amount"] for item in self.expenseDict["expense"])
        print("Total Income\t:\t", total_income)
        print("Total Expenses\t:\t", total_expense)

    def add_transaction_to_csv(self, amt, category, date, details, transaction_type):
        with open(self.csv_filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([amt, category, date, details, transaction_type])


def collectInput():
    amt = int(input("Enter the amount: "))
    category = input("Enter Category: ")
    date = input("Enter Date (DD/MM/YYYY): ")
    details = input("Enter description: ")
    return amt, category, date, details


myexpense = expenseTracker("expense_records.csv")

while True:
    print("...MY EXPENSE TRACKER...")
    print("1. Record Income")
    print("2. Record Expense")
    print("3. View Records")
    print("4. View My Spendings")
    print("5. Exit")

    choice = int(input("Enter your choice: ").strip())

    if choice == 1:
        print("Enter the details of income")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("income", amt, category, date, details)
    elif choice == 2:
        print("Enter the details of expense")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("expense", amt, category, date, details)
    elif choice == 3:
        myexpense.view_transactions()
    elif choice == 4:
        myexpense.calculate_transactions()
    elif choice == 5:
        exit()
    else:
        print("Invalid choice")
