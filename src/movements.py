from dataclasses import dataclass
import datetime

@dataclass
class Movement:
    """
    Represents a financial movement.

    Attributes:
        date (datetime.date): The transaction date.
        category (str): The spending or income category(e.g. food, rent, salary).
        amount (float): The quantity of the expense or income.
        type (str): If it is an expense or income.
        description (str): Optional description of the movement.
    """
    date: datetime.date
    category: str
    amount: float
    type: str
    description: str

    def __post_init__(self):
        """
        Validates the movement data after initialization.
        
        Raises:
            ValueError: If the amount is negative.
            ValueError: If the date is not in datetime format.
            ValueError: If the date is in future.
            TypeError: If the type is not a string.
            ValueError: If the type is not an 'expense' or 'income'
            TypeError: If the category is not a string.
            ValueError: If the category is empty. 
        """
        if self.amount < 0:
            raise ValueError("amount must be positive")
        if not isinstance(self.date, datetime.date):
            raise ValueError("Invalid date")
        if self.date > datetime.date.today():
            raise ValueError("Date cannot be in the future")
        if not isinstance(self.type, str):
            raise TypeError ("Please enter 'income' or 'expense' as the type")
        self.type = self.type.lower()
        if self.type not in ["income", "expense"]:
            raise ValueError("Please enter 'income' or 'expense' as the type")
        if not isinstance(self.category, str):
            raise TypeError("Please enter a correct category")
        self.category = self.category.lower()
        if not self.category:
            raise ValueError("Please enter a category")