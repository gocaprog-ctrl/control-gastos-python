"""Module proving the functions necessary to ensure
    the correctly functioning of the menu and security manipulation of the
    user."""

import datetime
from dataclasses import asdict
from src.storage import load_data, save_data
from src.movements import Movement

def view_balance():

    """Function to show the balance."""

    data = load_data()
    print(f"\nYour balance is: {data['balance']} $.")

def order_movements_by_date(movements):

    """Function to order the movements by date."""

    return sorted(movements, key=lambda x: x['date'], reverse=True)

def view_movements():

    """Function to show the movements."""

    data = load_data()

    while True:
        print("\n===Movements Menu===\n")
        print("1. View All Movements")
        print("\n2. View Movements by Category")
        print("\n3. View Movements by Type")
        print("\n0. Back to Main Menu")
        choice = input("\nSelect an option: ")
        if choice == "1":
            view_all_movements(data)
        elif choice == "2":
            view_movements_by_category(data)
        elif choice == "3":
            view_movements_by_type(data)
        elif choice == "0":
            break
        else:
            print("\nInvalid option.")

def view_all_movements(data):

    """Function to show all the movements."""

    if not data["movements"]:
        print("\nMovements not found.")
        return

    ordered_movements = order_movements_by_date(data["movements"])

    print("\n===Your Movements===\n")
    for movement in ordered_movements:
        date = movement['date']
        category = movement['category'].title()
        amount = movement['amount']
        description = movement['description']
        print(f"{date} - {category} - {amount}$ - {description}.\n")

def view_movements_by_category(data):

    """Function to show the movements by category."""

    if not data["movements"]:
        print("\nMovements not found.")
        return
    if not data["categories"]:
        print("\nCategories not found.")
        return

    ordered_movements = order_movements_by_date(data["movements"])

    while True:
        view_categories()
        try:
            category_choice = int(input("\nSelect Category (0 to cancel): "))
        except ValueError:
            print("\nPlease enter a valid number.")
            continue
        if category_choice == 0:
            print("\nOperation cancelled.")
            return
        if category_choice < 1 or category_choice > len(data["categories"]):
            print("\nThis category number did not exist.")
            continue
        selected_category = data["categories"][category_choice - 1]
        movement_found = False
        print(f"\n===Movements for {selected_category.title()}===\n")
        for movement in ordered_movements:
            if movement["category"] == selected_category:
                date = movement['date']
                category = movement['category'].title()
                amount = movement['amount']
                description = movement['description']
                print(f"{date} - {category} - {amount}$ - {description}.")
                movement_found = True
        if not movement_found:
            print(f"\nNo movements found for category: {selected_category.title()}.")

def view_movements_by_type(data):

    """Function to show the movements by type."""

    if not data["movements"]:
        print("\nMovements not found.")
        return

    ordered_movements = order_movements_by_date(data["movements"])

    while True:
        mov_choice = input("\nSelect Type 'expense' or 'income' (0 to cancel): ").strip().lower()

        if mov_choice == "0":
            print("\nOperation cancelled.")
            return
        if mov_choice not in ["expense", "income"]:
            print("\nInvalid value, please use 'income' or 'expense'")
            continue
        movement_found = False
        print(f"\n===Movements for {mov_choice.title()}===\n")
        for movement in ordered_movements:
            if movement["type"] == mov_choice:
                date = movement['date']
                category = movement['category'].title()
                amount = movement['amount']
                description = movement['description']
                print(f"{date} - {category} - {amount}$ - {description}.\n")
                movement_found = True
        if not movement_found:
            print(f"\nNo movements found for type: {mov_choice.title()}.")

def view_categories():

    """Funtion to show the categories with index."""

    data = load_data()
    if not data["categories"]:
        print("Categories not found.\n")
    else:
        print("\n===Your Categories===\n")
        for index,category in enumerate(data["categories"],start=1):
            print(f"{index} - {category.title()}\n")

def process_movement(data, mov_type, category, amount, description, date):

    """Function to process the user movements did."""

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

    """Function to add movement."""

    data = load_data()

    #Entrance
    while True:
        mov_type = input("\nWhich type 'expense' or 'income'? ").lower().strip()
        if mov_type in ["expense", "income"]:
            break
        print("\nInvalid value, please use 'income' or 'expense'")

    #Categories
    print ("\nAvailable Categories:\n")
    while True:
        for index, categories in enumerate(data["categories"], start=1):
            print(f"{index} - {categories.title()}\n" )
        try:
            category = int(input("Which category number? "))
        except ValueError:
            print("\nPlease, enter a positive number.\n")
            continue
        if category < 1 or category > len(data["categories"]):
            print("\nOut of range, please enter a number on index range.\n")
        else:
            break

    #Amount
    while True:
        try:
            amount = float(input("\nWhat amount? "))
        except ValueError:
            print("\nEnter a number.")
            continue
        if amount < 0:
            print("\nAmount must be positive.")
            continue
        break

    #Description
    description = input("\nAdd a description (optional): ")

    #Date
    while True:
        date_input = input("\nEnter the date (YYYY-MM-DD) or leave empty for today: ")
        if not date_input:
            date = datetime.date.today()
            break
        try:
            date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            if date > datetime.date.today():
                print("\nDate cannot be in the future.")
                continue
            break
        except ValueError:
            print("\nInvalid date. Please use YYYY-MM-DD format.")

    #Process
    try:
        category_index = category - 1
        category_name = data["categories"][category_index]
        data = process_movement(data, mov_type, category_name,
                        amount, description,date)
    except ValueError as e:
        print(f"\n{e}")
        return

    #Save
    save_data(data)
    print("\nSave successfully")

def add_new_category(data, new_category):

    """Add new category, logical part."""

    data["categories"].append(new_category)
    return data

def add_category():

    """Function add category, users inputs."""

    data = load_data()
    new_category = input("Which category will you add? ").lower()
    if not new_category:
        print("\nCategory cannot be empty.")
        return

    if not new_category.isalpha():
        print("\nCategory must contain only letters")
        return
    if new_category in data["categories"]:
        print("\nThis category already exists")
        return

    data = add_new_category(data, new_category)
    save_data(data)
    print("\nCategory added successfully.")


def remove_category(data, del_category):

    """Function to remove category, logical part."""

    data["categories"].pop(del_category -1)
    return data

def has_associated_movements(data, category):

    """Function to check if a category has associated movements."""

    for movement in data["movements"]:
        if movement["category"] == category:
            return True
    return False

def delete_category():

    """Function to delete category, users inputs"""

    data = load_data()

    while True:
        print("\n===Your Categories===\n")
        for index, category in enumerate(data["categories"], start=1):
            print(f"{index} - {category.title()}\n" )

        try:
            del_category = int(input("\nSelect number to delete (0 to cancel): "))
            selected_category = data["categories"][del_category - 1]
        except ValueError:
            print("\nPlease enter a valid number.")
            continue
        if del_category == 0:
            print("\nOperation cancelled.")
            return
        if del_category < 1 or del_category > len(data["categories"]):
            print("\nThis category number did not exist.")
            continue
        if has_associated_movements(data, selected_category):
            print(f"\nCategory {selected_category} cannot be deleted "
                  "because it has associated movements.")
            return


        data = remove_category(data, del_category)
        save_data(data)

        print("\nCategory Deleted. Saved Successfully.")
        break

def show_menu():

    """Function to show the menu options and interact with the user."""

    while True:
        print("\n=== Cost Control ===\n")
        print("1. View Balance")
        print("\n2. View Movements")
        print("\n3. Add Movements")
        print("\n4. View Categories")
        print("\n5. Add Category")
        print("\n6. Delete Category")
        print("\n7. Exit")
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
