from datetime import datetime
def create_csv_file():
    try:
        file = open("expenses.csv", "x")
        file.write("Date,Category,Amount,Note\n")
        file.close()

    except FileExistsError:
        pass


#First code
def add_expense():

    amount = input("Enter amount: ")

    print("\nSelect Category")
    print("1. Food")
    print("2. Transport")
    print("3. Entertainment")
    print("4. Other")

    category_choice = input("Enter category number: ")

    if category_choice == "1":
        category = "Food"

    elif category_choice == "2":
        category = "Transport"

    elif category_choice == "3":
        category = "Entertainment"

    else:
        category = "Other"

    note = input("Enter note: ")

    date = datetime.now().strftime("%d-%m-%Y")

    file = open("expenses.csv", "a")

    file.write(f"{date},{category},{amount},{note}\n")

    file.close()

    print("\nExpense Saved Successfully!")


#second code
def view_expenses():
    file = open("expenses.csv", "r")
    l = file.readlines()
    file.close()
    total = 0
    print(f"\n{'Date':<15}{'Category':<20}{'Amount':<10}{'Note'}")
    for line in l[1:]:  #the range mentioned is to skip the header row 
        line = line.strip()
        parts = line.split(",")
        date = parts[0]
        category = parts[1]
        amount = parts[2]
        note = parts[3]
        print(f"{date:<15}{category:<20}{amount:<10}{note}")
        total = total + int(amount)
    print("\nTotal Expenses =", total)

#Third code
def filter_expenses():

    print("\nSelect Category")
    print("1. Food")
    print("2. Transport")
    print("3. Entertainment")
    print("4. Other")

    choice = input("Enter category number: ")

    if choice== "1":
        selected_category = "Food"
    elif choice== "2":
        selected_category = "Transport"
    elif choice== "3":
        selected_category = "Entertainment"
    else:
        selected_category = "Other"

    file = open("expenses.csv", "r")
    lines = file.readlines()
    file.close()
    subtotal = 0
    print(f"\n{'Date':<15}{'Category':<20}{'Amount':<10}{'Note'}")

    for line in lines[1:]:
        line = line.strip()
        parts = line.split(",")
        date = parts[0]
        category = parts[1]
        amount = parts[2]
        note = parts[3]

        if category == selected_category:
            print(f"{date:<15}{category:<20}{amount:<10}{note}")
            subtotal = subtotal + int(amount)
    print("\nSubtotal =", subtotal)

#Main function(if its above the other code lines, it will show error)
def main():
    create_csv_file()
    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter By Category")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            print("You have exited now.")
            break
        else:
            print("Invalid Choice")
main()
