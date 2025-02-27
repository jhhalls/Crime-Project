import os
import pandas as pd
import numpy as np

def summarize_csv_folder(folder_path, generate_correlation=False):
    """
    Summarizes all CSV files in a folder on a column basis.
    
    Parameters:
    folder_path (str): Path to the folder containing CSV files.
    generate_correlation (bool): Whether to generate a correlation matrix for numerical columns.
    
    Outputs:
    - summary_report.csv: Column-wise statistics for each file.
    - schema_check.csv: Compares column names across files.
    - dtype_consistency.csv: Checks if columns have different data types across files.
    - correlation_matrix.csv (Optional): Correlation between numerical columns across files.
    """
    
    summary_list = []   # Stores column-wise statistics
    schema_dict = {}    # Stores schema of each file
    data_types_dict = {} # Stores data types for consistency check
    all_dataframes = []  # Stores data for correlation analysis (if enabled)

    # Loop through each file in the folder
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):  # Process only CSV files
            file_path = os.path.join(folder_path, file)
            
            # Read the CSV file
            df = pd.read_csv(file_path)
            
            print(f"Processing file: {file}")
            
            # Store schema info (column names)
            schema_dict[file] = set(df.columns)
            
            # Store data type info
            for col in df.columns:
                if col not in data_types_dict:
                    data_types_dict[col] = {}
                data_types_dict[col][file] = str(df[col].dtype)
            
            # Append for correlation analysis
            if generate_correlation:
                all_dataframes.append(df)

            # Process each column
            for col in df.columns:
                col_data = df[col]
                
                print(f"Processing column: {col}")
                
                # Calculate outlier threshold using IQR
                if pd.api.types.is_numeric_dtype(col_data):
                    Q1 = col_data.quantile(0.25)
                    Q3 = col_data.quantile(0.75)
                    IQR = Q3 - Q1
                    lower_bound = Q1 - 1.5 * IQR
                    upper_bound = Q3 + 1.5 * IQR
                    outlier_count = ((col_data < lower_bound) | (col_data > upper_bound)).sum()
                else:
                    outlier_count = None

                # Collect column-level statistics
                summary_list.append({
                    "File Name": file,
                    "Column": col,
                    "Data Type": col_data.dtype,
                    "Non-Null Count": col_data.count(),
                    "Mean": col_data.mean() if pd.api.types.is_numeric_dtype(col_data) else None,
                    "Median": col_data.median() if pd.api.types.is_numeric_dtype(col_data) else None,
                    "Std Dev": col_data.std() if pd.api.types.is_numeric_dtype(col_data) else None,
                    "Min": col_data.min() if pd.api.types.is_numeric_dtype(col_data) else None,
                    "Max": col_data.max() if pd.api.types.is_numeric_dtype(col_data) else None,
                    "Unique Values Count": col_data.nunique(),
                    "Most Frequent Value": col_data.mode()[0] if not col_data.mode().empty else None,
                    "Missing Values Count": col_data.isnull().sum(),
                    "Outlier Count": outlier_count
                })

    # Create a summary DataFrame and save it
    summary_df = pd.DataFrame(summary_list)
    summary_df.to_csv("summary_report.csv", index=False)

    print("✅ Summary Report saved as summary_report.csv")

    # Schema Consistency Check
    schema_check = pd.DataFrame.from_dict(schema_dict, orient="index").fillna("")
    schema_check.to_csv("schema_check.csv")

    print("✅ Schema Consistency Check saved as schema_check.csv")

    # Data Type Consistency Check
    dtype_df = []
    for col, files in data_types_dict.items():
        unique_types = set(files.values())
        dtype_df.append({
            "Column": col,
            "Files with Different Types": len(unique_types) > 1,
            "Data Types": files
        })

    dtype_check_df = pd.DataFrame(dtype_df)
    dtype_check_df.to_csv("dtype_consistency.csv", index=False)

    print("✅ Data Type Consistency Check saved as dtype_consistency.csv")

    # Generate correlation matrix if enabled
    if generate_correlation and all_dataframes:
        combined_df = pd.concat(all_dataframes, ignore_index=True)
        correlation_matrix = combined_df.corr()
        correlation_matrix.to_csv("correlation_matrix.csv")
        print("✅ Correlation Matrix saved as correlation_matrix.csv")
    # Display Outputs
    print("✅ Summary Report saved as summary_report.csv")
    print("✅ Schema Consistency Check saved as schema_check.csv")
    print("✅ Data Type Consistency Check saved as dtype_consistency.csv")
