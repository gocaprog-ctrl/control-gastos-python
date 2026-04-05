from storage import load_data, save_data
from movements import Movement
import datetime
from dataclasses import asdict

def view_balance():
    data = load_data()
    print(f"Your balance is: {data['balance']} $.")
def view_movements():
    data = load_data()
    if not data["movements"]:
        print("\nMovements not found.")
    else:
        print("\n===Your Last Movements===\n")
        for movement in data["movements"]:
            date = movement['date']
            category = movement['category'].title()
            amount = movement['amount']
            description = movement['description']
            print(f"{date} - {category} - {amount}$ - {description}.\n")

def view_categories():
    data = load_data()
    if not data["categories"]:
        print("Categories not found.\n")
    else:
        print("\n===Your Categories===\n")
        for category in data["categories"]:
            print(f"{category.title()}\n")

def process_movement(data, mov_type, category, amount, description, date):
    new_movement = Movement(date=date, type=mov_type, 
                            category=category, amount=amount, 
                            description=description)
    if new_movement.type == "expense":
        data["balance"] -= new_movement.amount
    elif new_movement.type == "income":
        data["balance"] += new_movement.amount
    movement_dict = asdict(new_movement)
    movement_dict["date"] = movement_dict["date"].isoformat()
    data["movements"].append(movement_dict)
    return data

def add_movement():
    try:
        data = load_data()
        date = datetime.date.today()
        mov_type = input("\nWhich type 'expense' or 'income'? ").lower().strip()
        if mov_type not in ["expense", "income"]:
            raise ValueError
        print ("\nAvailable Categories:")
        while True:
            for categories in data["categories"]:
                print(f"- {categories.title()}" )
            category = input("\nWhich category? \n").lower().strip()
            if category not in data["categories"]:
                print("\nWrong Category. Please try again.\n")
            else:
                break
        amount = float(input("\nWhat amount? "))
        description = input("\nAdd a description (optional): ")
        data = process_movement(data, mov_type, category, 
                            amount, description,date)
        save_data(data)
        print("\nSave successfully")
    except (TypeError, ValueError):
        print("\nWrong Value. Please enter a correct value")

def add_new_category(data, new_category):
        data["categories"].append(new_category)
        return data

def add_category():
    try:
        data = load_data()
        new_category = input("Which category will you add? ").lower()
        if new_category in data["categories"]:
            print("\nThis category already exists")
        else:
            data = add_new_category(data, new_category)
            save_data(data)
    except(TypeError, ValueError):
        print("Wrong value. Please enter a correct value")

def remove_category(data, del_category):
    data["categories"].remove(del_category)
    return data

def delete_category():
    try:
        data = load_data()
        del_category = input("Which category want delete? ").lower().strip()
        if del_category in data["categories"]:
            data = remove_category(data, del_category)
            print("\nCategory Deleted. Saved Successfully.")
            save_data(data)
        else:
            print("\nCategory not Deleted, please enter a valid category")
    except(TypeError, ValueError):
        print("Wrong category, write a correct category to delete.")

def show_menu():
    while True:
        print("\n=== Cost Control ===\n")
        print("1. View Balance")
        print("2. View Movements")
        print("3. Add Movements")
        print("4. View Category")
        print("5. Add Category")
        print("6. Delete Category")
        print("7. Exit")
        menu_input = input("\nIntroduce your option menu: ")
        if menu_input == "1":
            view_balance()
        elif menu_input == "2":
            view_movements()
        elif menu_input == "3":
            add_movement()
        elif menu_input == "4":
            view_categories()
        elif menu_input == "5":
            add_category()
        elif menu_input == "6":
            delete_category()
        elif menu_input == "7":
            break
        else:
            print("Wrong input, please introduce a valid value.")