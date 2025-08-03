import json
from datetime import datetime

# File to store data
DATA_FILE = "expenses.json"

# Load data from file
def load_expenses():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data to file
def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

# Add new expense
def add_expense():
    amount = float(input("Enter amount (₹): "))
    category = input("Enter category (e.g., Food, Rent, Travel): ")
    note = input("Optional note: ")
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": date
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")

# View all expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")
    for exp in expenses:
        print(f"{exp['date']} | ₹{exp['amount']} | {exp['category']} | {exp['note']}")

# Total amount spent
def total_spent():
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💸 Total spent: ₹{total:.2f}")

# Menu
def main():
    while True:
        print("\n📊 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Spent")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spent()
        elif choice == "4":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the app
main()
