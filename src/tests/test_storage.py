"""
Test to verify that data can be saved and loaded correctly
using the functions defined in storage.py.
"""
# Import functions responsible for saving and loading data to test them
from src.storage import save_data, load_data
import pytest

@pytest.fixture
def test_data():
    return {
        "balance": 0,
        "categories": [
            "food",
            "rent",
            "transport",
            "salary",
            "entertainment"
        ],
        "movements": [
            {
                "date": "2026-01-20",
                "category": "food",
                "amount": 12.5,
                "description": "Lunch"
            },
            {
                "date": "2026-01-21",
                "category": "transport",
                "amount": 3.2,
                "description": "Bus"
            }
        ]
    }

def test_save_and_load(test_data, tmp_path):
    file_path = tmp_path / "data.json"
    
    save_data(test_data, file_path=str(file_path))
    loaded_data = load_data(file_path=str(file_path))

    assert loaded_data == test_data



