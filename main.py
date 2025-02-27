import sys
import os
from src.data.load_data import load_csv_files
from src.data.clean_data import save_cleaned_data
from src.data.load_data import load_csv_files  
from src.data.preprocess import prepare_cleaned_data

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

# Define paths
raw_data_path = "/Users/rohit/Downloads/My ML playlist/crime_project/data/raw"
cleaned_data_path = "/Users/rohit/Downloads/My ML playlist/crime_project/data/cleaned_data"

# Clean data
clean_data_dict, filenames = prepare_cleaned_data(raw_data_path, cleaned_data_path)

print("✅ Cleaning and saving completed successfully!")