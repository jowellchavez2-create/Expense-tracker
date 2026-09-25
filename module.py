import os
import time
import json

def cls():
    os.system("cls" if os.name == 'nt' else 'clear')
def add(dict):
    cls()
    try:
        name = input("Insert the expense name to add: ")
        amount = int(input("Insert the expense amount to add: "))
        dict[name] = amount
        print("Expense Added")
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(dict, file)
        time.sleep(1.5)
    except ValueError:
        print("Error, insert a correct value")
        time.sleep(1.5)
def update(dict):
    cls()
    try:
        old_name = input("Insert the expense name to update: ")
        if old_name in dict:
            del dict[old_name]
        else:
            print("Error, the expense does not exist")
            time.sleep(1.5)
            update(dict)
        new_name = input("Insert the new name to add: ")
        new_amount = int(input("Insert the new amount to add: "))
        dict[new_name] = amount
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(dict, file)
        print("Expense updated")
        time.sleep(1.5)
    except ValueError:
        print("Error, insert a correct value")
        time.sleep(1.5)
def delete(dict):
    cls()
    try:
        name = input("Insert the expense name to delete: ")
        if name in dict:
            del dict[name]
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(dict, file)
            print("Expense deleted")
            time.sleep(1.5)
        else:
            print("Error, the expense does not exist")
            time.sleep(1.5)
            delete(dict)
    except ValueError:
        print("Error, insert a correct value")
        time.sleep(1.5)
def view(dict):
    cls()
    print(rf"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                   (\_/)
                   ( •_•)
                   / > ($)
            /- Expense Tracker -\
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    - ID -       - NAME -       - AMOUNT -
""")
    for index, (key, value) in enumerate(dict.items(),start=1):
        print(f"{index:^13} {key:^15} {value:^14}")
    print("")
    print(" (1) Leave ")
    print("")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
def total(dict):
    cls()
    print(rf"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                   (\_/)
                   ( •_•)
                   / > ($)
            /- Expense Tracker -\
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")
    print(f"Total expenses: ${sum(dict.values())}")
    print("")
    print(" (1) Leave ")
    print("")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
