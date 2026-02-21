import csv


def add_expense(amount, category, description, date):
    # This function allows us to add expenses directly from the app.
    expenses_list = [{'amount': amount, 'category': category, 'description': description, 'date': date}]
    fields = ['amount', 'category', 'description', 'date']


    with open('expenses.csv', 'a') as expenses_csv:
        expenses_writer = csv.DictWriter(expenses_csv, fieldnames=fields)

        for x in expenses_list:
            expenses_writer.writerow(x)
    
    print("\nYour expense has been added succesfully!")



def view_expenses():
    # This function allows us to view our expenses directly from the app.
    with open('expenses.csv', 'r') as expenses_csv:
        expenses_data = csv.DictReader(expenses_csv)

        for row in expenses_data:
            print("\nAmount:", row["amount"], "Category:", row["category"], "Description:", row["description"], "Date:", row["date"])



def calculate_total():
    # This function allows us to calculate the total of all the expenses directly from the app.
    total = 0

    with open('expenses.csv', 'r') as expenses_csv:
        reader = csv.DictReader(expenses_csv)

        for row in reader:
            total += float(row["amount"])

    
    print("\nYour expenses total is {}$.".format(total))



def delete_expense():
    # This function allows us to delete any expense data at choice.
    expenses = []

    with open('expenses.csv', 'r') as expenses_csv:
        reader = csv.reader(expenses_csv)

        for row in reader:
            expenses.append(row)

    print("\nExpenses:")

    for i in range(1, len(expenses)):
        print(i, "-", expenses[i])

    choice = int(input("Enter the number to delete: "))

    if choice > 0 and choice < len(expenses):
        expenses.pop(choice)
        print("Deleted successfully.")
    else:
        print("Invalid number.")
        return

    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for row in expenses:
            writer.writerow(row)






