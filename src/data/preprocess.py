# Data cleaning
import sys
import os
import re
from src.data.load_data import load_csv_files
# from src.data import load_data
from src.data.load_data import load_csv_files
from src.data.clean_data import (standardize_and_clean, remove_leading_numbers, remove_duplicates,
                        fix_data_types, save_cleaned_data)
from scripts.save_to_reports import save_dict_to_json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

def prepare_cleaned_data(raw_folder, cleaned_folder):
    """
    Executes the entire data cleaning pipeline and saves cleaned data.

    Args:
        raw_folder (str): Path to raw CSV files.
        cleaned_folder (str): Path to save cleaned files.

    Returns:
        dict: A dictionary where keys are cleaned filenames and values are DataFrames.
        list: A list of all cleaned filenames.
    """
    # Load raw data
    raw_data_dict, instructions = load_csv_files(raw_folder)
    
    cleaned_data_dict = {}  # Dictionary to store cleaned DataFrames

    # Process each file
    cleaned_filenames = []
    for filename, df in raw_data_dict.items():
        # Apply cleaning steps
        df = standardize_and_clean(df)
        df = remove_duplicates(df)
        df = fix_data_types(df)

        # Generate new filename by removing leading numbers
        new_filename = re.sub(r'^\d+_?', '', filename)
        cleaned_filepath = os.path.join(cleaned_folder, new_filename)

        # Save cleaned file
        # df.to_csv(cleaned_filepath, index=False)

        # Store cleaned DataFrame in dictionary
        cleaned_data_dict[new_filename] = df
        cleaned_filenames.append(new_filename)
    
    # Save cleaned data
    reports_loc = "/Users/rohit/Downloads/My ML playlist/crime_project/reports/decision_making_reports"
    save_dict_to_json(cleaned_data_dict, reports_loc, "raw_file_dict.json")

    # Print summary
    print(f"✅ {len(cleaned_filenames)} files cleaned and saved to {cleaned_folder}")
    
    return cleaned_data_dict, cleaned_filenames