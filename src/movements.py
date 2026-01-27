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