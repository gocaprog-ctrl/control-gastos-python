import pytest
import datetime
from movements import Movement

valid_types = ["income", "expense", "INCOME", "EXPENSE", "Income", "Expense"]
invalid_types = ["melon", "platano", "123", "incomee"]

def test_negative_value():
    with pytest.raises(ValueError):
        Movement(
            date = datetime.date(2026, 1, 20),
            category = "rent",
            amount = -10,
            type = "income",
            description = ""
        )

def test_invalid_date():
    with pytest.raises(ValueError):
        Movement(
            date = "2026-01-20",
            category = "rent",
            amount = 10,
            type = "income",
            description = ""
        )

def test_future_date_not_allowed():
    with pytest.raises(ValueError):
        Movement(
            date = datetime.date.today() + datetime.timedelta(days=1),
            category = "rent",
            amount = 10,
            type = "income",
            description = ""
        )

def test_correct_type_write():
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
    with pytest.raises(TypeError):
        Movement(
            date = datetime.date.today(),
            category = "rent",
            amount = 10,
            type = wrong_type,
            description = ""
        )
