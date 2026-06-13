def add_expense():
    while True:
        name = (input("ENTER THE NAME OF EXPENSE(or type 'done' to stop):")).strip().lower()
        if name=="done":
            break
        try:
            amount = float(input("ENTER THE AMOUNT:"))
            expenses[name] = amount
            print("EXPENSE ADDED SUCCESSFULLY!......")
        except ValueError:
            print("PLEASE ENTER A VALID AMOUNT!.....")
            continue


def view_expenses():
    if len(expenses) == 0:
        print("NO EXPENSES TO SHOW!.....")
    else:
        print("\n", "-"*5, "ALL EXPENSES", "-"*5)
        for i, (name, amount) in enumerate(expenses.items(), start=1):
            print(f"{i}. {name.capitalize()}: {amount}rs")


def show_total_expenses():
    total = sum(expenses.values())
    print("\n==========================")
    print("Total expense=", total, "rs")
    print("\n==========================")


def delete_expense():
    if not expenses:
        print("No expenses to delete!.....")
        return
    else:
        while True:
            if not expenses:
                print("All expenses deleted!.....")
                break
            print("\n--- CURRENT EXPENSES ---")
            view_expenses()
            try:
                choice = int(input("ENTER THE NUMBER OF THE EXPENSE YOU WANT TO DELETE(choose 0 to stop): "))
                if choice == 0:
                    break
                elif 1 <= choice <= len(expenses):
                    key = list(expenses.keys())[choice - 1]
                    deleted_amount = expenses.pop(key)
                    print(f"Expense '{key}' of {deleted_amount}rs deleted successfully!.....")
                else:
                    print("INVALID EXPENSE NUMBER!.....")
            except ValueError:
                print("PLEASE ENTER A VALID NUMBER!.....")
                continue



def highest_expense():
    if len(expenses)==0:
        print("No expenses to show!.....")
    else:
        highest = max(expenses.values())
        for name, amount in expenses.items():
            if amount == highest:
                print(f"HIGHEST EXPENSE:\n{name.capitalize()}: {amount}rs")


def search_expenses():
    if len(expenses)==0:
        print("No expenses to show!.....")
    else:
      try:  
        name=(input("Enter the name of expense you want to search:")).strip().lower()
        if name in expenses:
            print(f"{name.capitalize()}: {expenses[name]}rs")
        else:
            print("No expense found with that name!.....")

      except ValueError:
        print("ENTER VALID NAME!!!!!!!!") 

        

expenses = {}
while True:
 print("-"*5,"Expense Tracker","-"*5)
 print("-"*30)
 print("CHOOSE AN OPTION:")
 print("1. Add an expense")
 print("2. View expenses")
 print("3. Show total expenses")
 print("4. Delete an expense")
 print("5. Highest expense")
 print("6. SEARCH EXPENSES")
 print("7. Exit")

 try:
        choice = int(input("Enter your choice: "))
 except ValueError:
        print("\n[!] CRASH PREVENTED: Please enter numbers only (1-7)!")
        continue  # SKIPS THE REST OF THE LOOP AND SHOWS THE MENU AGAIN

 if choice==1:
     add_expense()
 elif choice==2:
     view_expenses()            
 elif choice==3:
     show_total_expenses()
 elif choice==4:
     delete_expense()
 elif choice==5:
     highest_expense()    
 elif choice==6:
     search_expenses()  
 elif choice==7: 
     print("THANK YOU FOR USING THE EXPENSE TRACKER!.....")
     break
 else:    
     print("INVALID CHOICE!.....")          