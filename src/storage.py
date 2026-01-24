import os
import json
# Root directory of the project, used to build absolute paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Path to the data directory
DATA_DIR = os.path.join(BASE_DIR, "data")
# Path to the data.json file
DATA_FILE_PATH = os.path.join(DATA_DIR, "data.json")

def load_data():
    """
    Loads application data from JSON file.
    If the data directory or file does not exist, they are created
    with default initial values.

    Returns:
        dict: Application data including balance, categories and movements.
    """
    #Ensure the data directory exists
    if not os.path.isdir(DATA_DIR):
        os.mkdir(DATA_DIR)
    # If the data file does not exist, create it with default values
    if not os.path.isfile(DATA_FILE_PATH):
        initial_data = {
            "balance": 0,
            "categories": [
                "food",
                "rent",
                "transport",
                "salary",
                "entertainment"
            ],
            "movements": []
        }
        # Write the initial data to the JSON file
        with open(DATA_FILE_PATH, "w") as file:
            json.dump(initial_data, file, indent=4)

        return initial_data
    # If the file exist, read and return its contents
    with open(DATA_FILE_PATH, "r") as file:
        data = json.load(file)
        
    return data

def save_data(data):
    """
    Save the application data to the JSON file.

    Args:
        data(dict): Dictionary containing the current application state,
        including balance, categories and movements.
    """
    with open(DATA_FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)