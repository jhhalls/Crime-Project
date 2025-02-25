import os
import kagglehub

# Define the local directory to download the dataset
local_path = "/Users/rohit/Downloads/My ML playlist/crime_project/data/raw/raw_data_from_kaggle"  

# Check if the directory exists, if not, create it
if not os.path.exists(local_path):
    os.makedirs(local_path)
    print(f"Directory created at: {local_path}")
else:
    print(f"Directory already exists: {local_path}")

# Download dataset to the specified location
path = kagglehub.dataset_download("rajanand/crime-in-india", path=local_path)

print("Dataset downloaded to:", path)