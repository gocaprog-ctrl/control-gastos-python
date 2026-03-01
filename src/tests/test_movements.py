import pytest
import datetime
from movements import Movement

valid_types = ["income", "expense", "INCOME", "EXPENSE", "Income", "Expense"]
invalid_types = ["melon", "platano", "123", "incomee"]

def test_negative_value():
    """
    Test to validate a negative value fails.
    """
    with pytest.raises(ValueError):
        Movement(
            date = datetime.date(2026, 1, 20),
            category = "rent",
            amount = -10,
            type = "income",
            description = ""
        )

def test_invalid_date():
    """
    Test to validate a incorrect format fails.
    """
    with pytest.raises(ValueError):
        Movement(
            date = "2026-01-20",
            category = "rent",
            amount = 10,
            type = "income",
            description = ""
        )

def test_future_date_not_allowed():
    """
    Test to validate a future date fails.
    """
    with pytest.raises(ValueError):
        Movement(
            date = datetime.date.today() + datetime.timedelta(days=1),
            category = "rent",
            amount = 10,
            type = "income",
            description = ""
        )

def test_correct_type_write():
    """
    Test to validate a correct type value.
    """
    for type_value in valid_types:
        movement = Movement(
            date = datetime.date.today(),
            category = "rent",
            amount = 10,
            type = type_value,
            description = ""
        )
        assert movement.type == type_value.lower()

@pytest.mark.parametrize("invalid_type", invalid_types)
def test_invalid_type(invalid_type):
    """
    Test to validate a type is invalid and fails.
    Args:
        invalid_type (list): List with invalid values.  
    """
    with pytest.raises(ValueError):
        Movement(
            date = datetime.date.today(),
            category = "rent",
            amount = 10,
            type = invalid_type,
            description = ""
        )

@pytest.mark.parametrize("wrong_type", [None, 123, [], {}])
def test_type_not_string(wrong_type):
    """
    Test to validate type is not a string fails. 
    
    Args:
        wrong_type (None | int | list | dict): No valid values
    """
    with pytest.raises(TypeError):
        Movement(
            date = datetime.date.today(),
            category = "rent",
            amount = 10,
            type = wrong_type,
            description = ""
        )

@pytest.mark.parametrize("wrong_category", [None, 123, [], {}])
def test_category_not_string(wrong_category):
    """
    Test to validate category is not a string fails. 
    
    Args:
        wrong_category (None | int | list | dict): No valid values
    """
    with pytest.raises(TypeError):
        Movement(
            date = datetime.date.today(),
            category = wrong_category,
            amount = 10,
            type = "income",
            description = "" 
        )

def test_empty_category():
    """
    Test to validate empty category fails. 
    """
    with pytest.raises(ValueError):
        Movement(
            date = datetime.date.today(),
            category = "",
            amount = 10,
            type = "income",
            description = ""
        )