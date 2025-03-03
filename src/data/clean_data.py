import pandas as pd
import os
import re

import pandas as pd

def standardize_and_clean(df):
    """
    Standardizes column names to a consistent format (lowercase, underscores instead of spaces)
    and removes leading and trailing whitespace from column names and all elements in a DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Cleaned and standardized DataFrame.
    """
    print("\nBefore standardizing and cleaning, the columns are:")
    print(df.columns)

    # Remove leading and trailing whitespace from column names
    df.columns = df.columns.str.strip()

    # Standardize column names to lowercase with underscores instead of spaces
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Remove leading and trailing whitespace from all elements in the DataFrame
    df = df.applymap(lambda x: str(x).strip() if pd.notna(x) else x)

    print("\nAfter standardizing and cleaning, the columns are:")
    print(df.columns)
    return df


def remove_leading_numbers(filename: str) -> str:
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

def remove_duplicates(df):
    """
    Removes duplicate rows from the DataFrame.
    Args:
        df (pd.DataFrame): The input DataFrame from which duplicate rows are to be removed.
    Returns:
        pd.DataFrame: A DataFrame with duplicate rows removed.
    """
    print("\nBefore removing duplicates, the shape of the DataFrame is:", df.shape)
    # Utilize the built-in drop_duplicates method to remove duplicate rows
    df = df.drop_duplicates()
    print("\nAfter removing duplicates, the shape of the DataFrame is:", df.shape)
    return df

def fix_data_types(df):
    """Converts columns to appropriate data types."""
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            print(f"Conversion failed for column: {col}")
            pass  # Ignore if conversion is not possible
    print("\nAfter fixing data types, the DataFrame is:")
    print(df.info())
    return df

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
        cleaned_filenames.append({"Cleaned File Name": new_file_name})  # Store new filename
        print(f"✅ Saved cleaned file: {cleaned_file_path}")

    # Save cleaned filenames as a CSV file
    cleaned_filenames_df = pd.DataFrame(cleaned_filenames)  
    list_file_path = os.path.join(output_dir, "cleaned_file_list.csv")
    cleaned_filenames_df.to_csv(list_file_path, index=False)  # Save CSV without index

    print(f"📜 List of cleaned files saved to: {list_file_path}")