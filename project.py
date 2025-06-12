import json

data_file = 'budget_data.json'

def load_data():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"income": 0, "expenses": []}

def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file)

def add_income(data):
    try:
        income = float(input("Enter your income: $"))
        data['income'] = income
        save_data(data)
        print(f"Income of ${income} added!")
    except ValueError:
        print("invalid input, please enter a valid number.")

def add_expense(data):
    try:
        expense = float(input("Enter expense amount: $"))
        category = input("Enter expense category: ")
        data['expenses'].append({"amount": expense, "category": category})
        save_data(data)
        print(f"Expense of ${expense} for {category} added!")
    except ValueError:
        print("Invalid input, please enter a valid number.")

def view_summary(data):
    total_expenses = sum(exp['amount'] for exp in data['expenses'])
    remaining_balance = data['income'] - total_expenses
    print("\n---- Budget Summary ---")
    print(f"Total Income: ${data['income']}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Remaining Balance: ${remaining_balance}")
    print("\nExpenses:")
    for exp in data['expenses']:
        print(f"- ${exp['amount']} for {exp['category']}")
    print("----------------------")

def clear_budget(data):
    confirm = input("Are you sure you want to clear all budget data? (yes/no): ").lower()
    if confirm == 'yes':
        data['income'] = 0
        data['expenses'] = []
        save_data(data)
        print("Budget data cleared!")
    else:
        print("Clear budget canceled.")

def main():
    data = load_data()

    while True:
        print("\n1. Add Income")
        print("2. Add Expenses")
        print("3. View Summary")
        print("4. Clear Budget")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            view_summary(data)
        elif choice == '4':
            clear_budget(data)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
        
