import pandas as pd
import os
import re

def clean_whitespace(df):
    """
    Removes leading and trailing spaces from column names and all elements in a DataFrame,
    irrespective of their datatype.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame with stripped whitespace.
    """
    df.columns = df.columns.str.strip()
    df = df.applymap(lambda x: str(x).strip() if pd.notna(x) else x)
    return df


def remove_leading_numbers(filename):
    """
    Removes leading numbers and any following underscores from a filename 
    while preserving the file extension.

    Args:
        filename (str): Original filename.

    Returns:
        str: Cleaned filename.
    """
    name, ext = os.path.splitext(filename)  # Split filename and extension
    cleaned_name = re.sub(r'^\d+_?', '', name).lstrip()  # Remove leading numbers + optional underscore
    return f"{cleaned_name}{ext}"  # Reconstruct filename with extension

def save_cleaned_data(data_dict, output_dir="data/cleaned_data"):
    """
    Saves cleaned DataFrames to the specified directory with renamed files
    (removing leading numbers) and stores the list of cleaned filenames.

    Args:
        data_dict (dict): Dictionary where keys are filenames and values are DataFrames.
        output_dir (str): Directory to save cleaned data.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the folder if it doesn't exist

    cleaned_filenames = []  # Store new filenames

    for file_name, df in data_dict.items():
        new_file_name = remove_leading_numbers(file_name)  # Rename file
        cleaned_file_path = os.path.join(output_dir, new_file_name)
        
        df.to_csv(cleaned_file_path, index=False)  # Save CSV without index
        cleaned_filenames.append(new_file_name)  # Store new filename
        print(f"✅ Saved cleaned file: {cleaned_file_path}")

    # Save cleaned filenames to a text file
    list_file_path = os.path.join(output_dir, "cleaned_file_list.txt")
    with open(list_file_path, "w") as file:
        file.writelines("\n".join(cleaned_filenames))

    print(f"📜 List of cleaned files saved to: {list_file_path}")