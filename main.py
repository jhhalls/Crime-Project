import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from src.data.load_data import load_csv_files
from src.data.data_cleaning import clean_whitespace, save_cleaned_data
from src.data.load_data import load_csv_files  

# path to csv file location
csv_directory = "/Users/rohit/Downloads/My ML playlist/crime_project/data/raw"

raw_data, instructions = load_csv_files(csv_directory)  # Dictionary of {filename: DataFrame}
print(f"The raw data is:\n{raw_data}")
print(f"\nFollow the below instructions on how to access the data files :\n{instructions}")

# Clean data
cleaned_data = {file: clean_whitespace(df) for file, df in raw_data.items()}

# Save cleaned data to 'data/cleaned_data'
save_cleaned_data(cleaned_data)

print("✅ Cleaning and saving completed successfully!")