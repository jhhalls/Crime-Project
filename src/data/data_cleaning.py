import pandas as pd
import os

def clean_whitespace(df):
    """
    Removes leading and trailing spaces from column names and all elements in a DataFrame,
    irrespective of their datatype. This is necessary because some CSV files may have
    leading or trailing spaces in the column names or data.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame with stripped whitespace.
    """
    # Remove leading and trailing spaces from column names
    df.columns = df.columns.str.strip()

    # Remove leading and trailing spaces from all elements in the DataFrame
    # This includes strings, floats, integers, etc.
    # We use the applymap function to apply the lambda function to every element
    # in the DataFrame. The lambda function takes a value and returns the
    # stripped string if the value is not a NaN, otherwise it returns the
    # original value.
    df = df.applymap(lambda x: str(x).strip() if pd.notna(x) else x)

    return df

def save_cleaned_data(data_dict, output_dir="data/cleaned_data"):
    """
    Saves cleaned DataFrames to the specified directory.

    Args:
        data_dict (dict): Dictionary where keys are filenames and values are DataFrames.
        output_dir (str): Directory to save cleaned data.
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over the data dictionary and save each DataFrame
    for file_name, df in data_dict.items():
        cleaned_file_path = os.path.join(output_dir, file_name)
        df.to_csv(cleaned_file_path, index=False)  # Save CSV without index
        print(f"Saved cleaned file: {cleaned_file_path}")
