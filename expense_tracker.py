import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


# Load data
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# Add transaction
def add_transaction():
    t_type = input("Type (income/expense): ").lower()
    amount = float(input("Amount: "))
    description = input("Description: ")

    transaction = {
        "type": t_type,
        "amount": amount,
        "description": description,
        "date": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    }

    data = load_data()
    data.append(transaction)
    save_data(data)

    print("Transaction added successfully!\n")


# View all transactions
def view_transactions():
    data = load_data()

    if not data:
        print("No transactions found.\n")
        return

    for i, t in enumerate(data, start=1):
        print(f"{i}. {t['date']} | {t['type']} | R{t['amount']} | {t['description']}")


# Show balance
def show_balance():
    data = load_data()

    income = sum(t["amount"] for t in data if t["type"] == "income")
    expense = sum(t["amount"] for t in data if t["type"] == "expense")

    balance = income - expense

    print("\n--- SUMMARY ---")
    print(f"Total Income: R{income}")
    print(f"Total Expenses: R{expense}")
    print(f"Balance: R{balance}\n")


# Menu
def menu():
    while True:
        print("=== EXPENSE TRACKER ===")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. Show balance")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            show_balance()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option\n")


menu()