import os
import json
# Root directory of the project, used to build absolute paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Path to the data directory
DATA_DIR = os.path.join(BASE_DIR, "data")
# Path to the data.json file
DATA_FILE_PATH = os.path.join(DATA_DIR, "data.json")

def load_data(file_path: str =DATA_FILE_PATH) -> dict:
    """
    Load application data from a JSON file.

    If the data directory or file does not exist, they are created
    with default initial values.

    Args:
        file_path (str): Path to the JSON data file.

    Returns:
        dict: Application data including balance, categories and movements.
    """
    data_dir = os.path.dirname(file_path)

    #Ensure the data directory exists
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir, exist_ok=True)
    # If the data file does not exist, create it with default values
    if not os.path.isfile(file_path):
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
        with open(file_path, "w") as file:
            json.dump(initial_data, file, indent=4)

        return initial_data
    # If the file exist, read and return its contents
    with open(file_path, "r") as file:
        data = json.load(file)
        
    return data

def save_data(data: dict, file_path: str = DATA_FILE_PATH) -> None:
    """
    Save the application data to a JSON file.

    Args:
        data (dict): Dictionary containing the current application state,
            including balance, categories and movements.
        file_path (str): Path to the JSON data file.
    """
    data_dir = os.path.dirname(file_path)
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)