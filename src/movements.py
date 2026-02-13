from dataclasses import dataclass
import datetime

@dataclass
class Movement:
    date: datetime.date
    category: str
    amount: float
    type: str
    description: str

    def __post_init__(self):
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