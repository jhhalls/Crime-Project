import pandas as pd
import os

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

def save_cleaned_data(data_dict, output_dir="data/cleaned_data"):
    """
    Saves cleaned DataFrames to the specified directory.

    Args:
        data_dict (dict): Dictionary where keys are filenames and values are DataFrames.
        output_dir (str): Directory to save cleaned data.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the folder if it doesn't exist

    for file_name, df in data_dict.items():
        cleaned_file_path = os.path.join(output_dir, file_name)
        df.to_csv(cleaned_file_path, index=False)  # Save CSV without index
        print(f"Saved cleaned file: {cleaned_file_path}")