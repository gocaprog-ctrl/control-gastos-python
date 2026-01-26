"""
Tests for storage persistence functions.

These tests verify that application data can be correctly
saved to and loaded from a JSON file using the storage module.
"""

# Import functions responsible for saving and loading data to test them
from src.storage import save_data, load_data
import pytest
import json

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
    """
    Test that verifies data saved to a JSON file can be loaded back correctly.

    The test saves application data to a temporary file using save_data,
    loads it using load_data, and checks that the loaded data matches
    the original data.
    """
    # Arrange: Create a temporary file path for the test
    file_path = tmp_path / "data.json"

    # Act: save data to disk and load it back
    save_data(test_data, file_path=str(file_path))
    loaded_data = load_data(file_path=str(file_path))

    # Asserts: loaded data must match the original data
    assert loaded_data == test_data

def test_load_data_when_file_missing(tmp_path):
    """
    Ensure that load_data creates the data directory and data.json file
    when the file does not exist.
    """
    # Arrange: create a temporary path where data.json does NOT exist yet
    file_path = tmp_path / "data.json"
    
    # Act: call load_data, which should create the directory and the file
    load_data(file_path=str(file_path))

    # Asserts: verify that the directory and the file were created
    assert file_path.parent.is_dir()
    assert file_path.is_file()


def test_load_data_when_file_is_corrupt(tmp_path):
    """
    If the data file exists but contains invalid JSON,
    load_data should recover and return default data.
    """
    # Arrange
    file_path = tmp_path / "data.json"
    with open(file_path, "w") as file:
        file.write("this is not valid json")

    # Act
    loaded_data = load_data(file_path=str(file_path))

    # Assert
    assert loaded_data["balance"] == 0
    assert loaded_data["categories"]
    assert loaded_data["movements"] == []

def test_pytest_is_seeing_this():
    assert True
