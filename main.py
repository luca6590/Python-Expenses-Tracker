from functions import add_expense, view_expenses, calculate_total, delete_expense

while True:
    choice = input(""" \n
    Welcome to the Expenses Tracker! Please type the number for your action:
               
    1. Add expense
    2. View all expenses
    3. Show total spent
    4. Delete data
               
    """)


    if choice == '1':
        amount = float(input("\nEnter the amount: "))
        category = input("Enter the category: ")
        description = input("Enter the description: ")
        date = input("Enter the date (DD-MM-YYYY): ")

        add_expense(amount, category, description, date)

        exit_choice = input("\nDo you want to exit the app?(yes or no)")
        if exit_choice == 'yes':
            break
        else:
            pass
    elif choice == '2':
        view_expenses()

        exit_choice = input("\nDo you want to exit the app?(yes or no)")
        if exit_choice == 'yes':
            break
        else:
            pass
    elif choice == '3':
        calculate_total()

        exit_choice = input("\nDo you want to exit the app?(yes or no)")
        if exit_choice == 'yes':
            break
        else:
            pass
    elif choice == '4':
        delete_expense()

        exit_choice = input("\nDo you want to exit the app?(yes or no)")
        if exit_choice == 'yes':
            break
        else:
            pass