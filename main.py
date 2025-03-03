import sys
import os
from src.data.load_data import load_csv_files
from src.data.clean_data import save_cleaned_data
from src.data.load_data import load_csv_files  
from src.data.preprocess import prepare_cleaned_data
from scripts.summary import generate_csv_summary


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

# Define paths
raw_data_path = "/Users/rohit/Downloads/My ML playlist/crime_project/data/raw"
cleaned_data_path = "/Users/rohit/Downloads/My ML playlist/crime_project/data/cleaned_data"

# push Clean data to cleaned_data folder
clean_data_dict, filenames = prepare_cleaned_data(raw_data_path, cleaned_data_path)


save_cleaned_data(clean_data_dict)

print("✅ Cleaning and saving completed successfully!")

# # Summarize data
# summarize_data_path = f"/Users/rohit/Downloads/My ML playlist/crime_project/reports"
# generate_csv_summary(input_folder_path=cleaned_data_path, 
#                      output_folder_path=summarize_data_path, 
#                      include_correlation_matrix=True)

# print("✅ Data summary generated successfully!")
