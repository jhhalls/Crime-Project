import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from src.data.load_data import load_csv_files

# path to csv file location
csv_directory = "/Users/rohit/Downloads/My ML playlist/crime_project/data/raw/raw_data_from_kaggle"

raw_data, instructions = load_csv_files(csv_directory)
print(f"The raw data is:\n{raw_data}")
print(f"\nFollow the below instructions on how to access the data files :\n{instructions}")

