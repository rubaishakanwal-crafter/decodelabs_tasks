# Expense Tracker

print("========== Expense Tracker ==========")

total_spent = 0

while True:
    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    expense = float(expense)

    total_spent = total_spent + expense

print("\n========== Summary ==========")
print(f"Total Spent: Rs. {total_spent:.2f}")
print("Thank you for using Expense Tracker!")
