import json

FILENAME = "expenses.json"

def load_expenses():
    try:
        with open(FILENAME,"r") as file:
            json.loads(file)
    except FileNotFoundError:
        return []
def save_expenses():
    with open(FILENAME,"w") as file:
        json.dump(expenses, file)
expenses = load_expenses()





while True:
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Delete expense")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        try:
            amount = float(input("amount: "))
        except ValueError:
            print("Enter a valid number.")
            continue
        category = input("Category: ")
        description = input("Description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        expenses.append(expense)
        save_expenses()
        print("Expense added.")
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses  yet")
        else:
            for i , expense in enumerate(expenses,1):
                print(f"{i}. {expense['category']} - {expense['amount']} - {expense['description']}")
    elif choice == "3":
        total = 0
        for expense in expenses:
            total = total + expense["amount"]
        print(f"Total spent = {total}")

    elif choice == "4":
        if len(expenses) == 0:
            print("No expense to delete.")
        else:
            for i , expense in enumerate(expenses,1):
                print(f"{i}. {expense['category']} - {expense['amount']} - {expense['description']}")
            try:
                number = int(input("Enter the number you want to delete: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if 1 <= number <= len(expenses):
                expenses.pop(number - 1)
                save_expenses()
                print("Expense deleted successfully.")
            else:
                print("Invalid number:")
        
    elif choice == "5":
        print("Quitting the program...")
        save_expenses()
        break
    else:
        print("Invalid choice, try again.")