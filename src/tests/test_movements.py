import pytest
import datetime
from movements import Movement

def test_negative_value():
    with pytest.raises(ValueError):
        Movement(
            date = datetime.date(2026, 1, 20),
            category = "rent",
            amount = -10,
            type= "income",
            description = ""
        )

def test_invalid_date():
    with pytest.raises(ValueError):
        Movement(
            date = "2026-01-20",
            category = "rent",
            amount = 10,
            type= "income",
            description = ""
        )

def test_future_date_not_allowed():
    with pytest.raises(ValueError):
        Movement(
            date = datetime.date.today() + datetime.timedelta(days=1),
            category = "rent",
            amount = 10,
            type= "income",
            description = ""
        )
