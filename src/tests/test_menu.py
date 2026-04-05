import datetime
from menu import process_movement, add_new_category, remove_category

def test_income_increase_balace():
    # Arrange
    inital_balance = 100
    amount_to_add = 50
    expected_balance = inital_balance + amount_to_add
    
    data = {"balance": inital_balance,
            "categories": ["food","rent","transport","salary","entertainment","extras"],
    "movements": []}
    
    # Act
    data_result = process_movement(data, mov_type="income", category="salary",
                                amount=amount_to_add, description="test", 
                                date=datetime.date.today())
    
    # Assert
    assert data_result["balance"] == expected_balance
    
def test_expense_decrease_balance():
    # Arrange
    inital_balance = 100
    amount_to_decrease = 50
    expected_balance = inital_balance - amount_to_decrease
    
    data = {"balance": inital_balance,
            "categories": ["food","rent","transport","salary","entertainment","extras"],
    "movements": []}
    
    # Act
    data_result = process_movement(data, mov_type="expense", category="food",
                                amount=amount_to_decrease, description="test",
                                date=datetime.date.today())
    # Assert
    assert data_result["balance"] == expected_balance

def test_add_new_category():
    # Arrange
    new_category_name = "sports"
    
    data = {"balance": 100,
            "categories": ["food", "rent", "transport", "salary","extras"],
            "movements": []}
    
    initial_count = len(data["categories"])
    
    # Act
    data_result = add_new_category(data, new_category=new_category_name)
    
    # Assert
    assert new_category_name in data_result["categories"]
    assert len(data_result["categories"]) == initial_count + 1

def test_remove_category():
    # Arrange
    remove_category_name = "food"
    
    data = {"balance": 100,
            "categories": ["food", "rent", "transport", "salary","extras"],
            "movements": []}
    
    initial_count = len(data["categories"])
    
    # Act
    data_result = remove_category(data, del_category=remove_category_name)
    
    # Assert
    assert remove_category_name not in data_result["categories"]
    assert len(data_result["categories"]) == initial_count - 1