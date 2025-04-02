import json
import os

def save_dict_to_json(data_dict, save_path, filename):
    """
    Saves a dictionary as a JSON file at the specified location.
    
    Parameters:
    - data_dict (dict): The dictionary to save.
    - save_path (str): The directory where the file should be saved.
    - filename (str): The name of the JSON file (should end with .json).
    
    Returns:
    - str: Full path of the saved JSON file.
    """
    # Ensure the save path exists
    os.makedirs(save_path, exist_ok=True)
    
    # Full file path
    file_path = os.path.join(save_path, filename)
    
    # Save dictionary as JSON
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data_dict, json_file, indent=4, ensure_ascii=False)  # Pretty print JSON
    
    print(f"Dictionary successfully saved to: {file_path}")
    return file_path  # Return the file path for reference