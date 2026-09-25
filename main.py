import os
import time
import module
import json

if os.path.isfile("data.json"):
    with open("data.json", "r", encoding="utf-8") as file:
        expenses = json.load(file)
else:
    expenses = {}
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(expenses, file)

def goback():
    try:
        selection = int(input(" ---> "))
        if selection == 1:
            pass
        else:
            print("Error, please insert a correct number")
            time.sleep(1.5)
    except ValueError:
        print("Error, insert a correct value")
        time.sleep(1.5)
def cls():
    os.system("cls" if os.name == 'nt' else 'clear')
def main():
    cls()
    print(rf"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                   (\_/)
                   ( •_•)
                   / > ($)
            /- Expense Tracker -\
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

 (1) Add Expense     |  (4) View All Expenses
 (2) Update Expense  |  (5) Total Summary
 (3) Delete Expense  |  (6) Exit

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")
    try:
        option = int(input(" ---> "))
    except ValueError:
        print("Error, please insert a correct number")
        time.sleep(1.5)
    else:
        if option == 1:
            module.add(expenses)
        elif option == 2:
            module.update(expenses)
        elif option == 3:
            module.delete(expenses)
        elif option == 4:
            module.view(expenses)
            goback()
        elif option == 5:
            module.total(expenses)
            goback()
        elif option == 6:
            quit()
        else:
            print("Error, please insert a correct number")
            time.sleep(1.5)
    
while True:
    main()