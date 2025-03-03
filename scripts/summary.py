from typing import List, Dict, Optional, Union
import os
import pandas as pd
import numpy as np


def generate_csv_summary(
    input_folder_path: str, 
    output_folder_path: str, 
    include_correlation_matrix: bool = False
) -> None:
    """
    Generates a summary of all CSV files in a folder on a column-wise basis.
    
    Parameters:
        input_folder_path (str): Path to the folder containing CSV files.
        output_folder_path (str): Path where summary reports will be saved.
        include_correlation_matrix (bool): If True, generates a correlation matrix for numerical columns.
        
    Outputs:
        column_summary.csv: Provides statistics for each column in every file.
        schema_comparison.csv: Compares column names across all CSV files.
        datatype_consistency.csv: Checks if columns have different data types across files.
        correlation_matrix.csv (Optional): Correlation analysis of numerical columns.
    """

    os.makedirs(output_folder_path, exist_ok=True)

    column_statistics_list: List[Dict[str, Union[str, int, float, None]]] = []   # Stores summary statistics for each column
    file_column_mapping: Dict[str, set] = {}      # Stores column names for each file
    column_datatype_mapping: Dict[str, Dict[str, str]] = {}  # Stores data types for consistency check
    dataframe_collection: List[pd.DataFrame] = []     # Stores data for correlation analysis (if enabled)

    csv_files = [f for f in os.listdir(input_folder_path) if f.endswith(".csv")]

    if not csv_files:
        print("⚠️ No CSV files found in the folder.")
        return
    
    for filename in csv_files:
        file_path = os.path.join(input_folder_path, filename)

        try:
            dataframe = pd.read_csv(file_path)

            if dataframe.empty:
                print(f"⚠️ Skipping empty file: {filename}")
                continue

            file_column_mapping[filename] = set(dataframe.columns)

            for column_name in dataframe.columns:
                if column_name not in column_datatype_mapping:
                    column_datatype_mapping[column_name] = {}
                column_datatype_mapping[column_name][filename] = str(dataframe[column_name].dtype)

            dataframe_collection.append(dataframe)

            for column_name in dataframe.columns:
                column_data = dataframe[column_name]

                if column_data.count() == 0:
                    continue

                outlier_count = None

                if pd.api.types.is_numeric_dtype(column_data):
                    first_quartile = column_data.quantile(0.25)
                    third_quartile = column_data.quantile(0.75)
                    interquartile_range = third_quartile - first_quartile
                    lower_threshold = first_quartile - 1.5 * interquartile_range
                    upper_threshold = third_quartile + 1.5 * interquartile_range
                    outlier_count = ((column_data < lower_threshold) | (column_data > upper_threshold)).sum()

                column_statistics_list.append({
                    "File Name": filename,
                    "Column Name": column_name,
                    "Data Type": column_data.dtype,
                    "Non-Null Count": column_data.count(),
                    "Mean": column_data.mean() if pd.api.types.is_numeric_dtype(column_data) else None,
                    "Median": column_data.median() if pd.api.types.is_numeric_dtype(column_data) else None,
                    "Standard Deviation": column_data.std() if pd.api.types.is_numeric_dtype(column_data) else None,
                    "Minimum Value": column_data.min() if pd.api.types.is_numeric_dtype(column_data) else None,
                    "Maximum Value": column_data.max() if pd.api.types.is_numeric_dtype(column_data) else None,
                    "Unique Value Count": column_data.nunique(),
                    "Most Frequent Value": column_data.mode()[0] if not column_data.mode().empty else None,
                    "Missing Value Count": column_data.isnull().sum(),
                    "Outlier Count": outlier_count
                })

        except Exception as e:
            print(f"❌ Error processing file {filename}: {e}")

    if not column_statistics_list:
        print("⚠️ No valid data found in CSV files. No summary will be generated.")
        return

    column_summary_df = pd.DataFrame(column_statistics_list)
    column_summary_file = os.path.join(output_folder_path, "column_summary.csv")
    column_summary_df.to_csv(column_summary_file, index=False)
    print(f"✅ Column Summary saved at: {column_summary_file}")

    schema_comparison_df = pd.DataFrame.from_dict(file_column_mapping, orient="index").fillna("")
    schema_comparison_file = os.path.join(output_folder_path, "schema_comparison.csv")
    schema_comparison_df.to_csv(schema_comparison_file)
    print(f"✅ Schema Comparison saved at: {schema_comparison_file}")

    datatype_consistency_records = []
    for column_name, file_mapping in column_datatype_mapping.items():
        unique_data_types = set(file_mapping.values())
        datatype_consistency_records.append({
            "Column Name": column_name,
            "Inconsistent Data Types Across Files": len(unique_data_types) > 1,
            "Data Types by File": file_mapping
        })

    datatype_consistency_df = pd.DataFrame(datatype_consistency_records)
    datatype_consistency_file = os.path.join(output_folder_path, "datatype_consistency.csv")
    datatype_consistency_df.to_csv(datatype_consistency_file, index=False)
    print(f"✅ Data Type Consistency Report saved at: {datatype_consistency_file}")

    if include_correlation_matrix and dataframe_collection:
        combined_dataframe = pd.concat(dataframe_collection, ignore_index=True)
        
        numeric_columns = combined_dataframe.select_dtypes(include=[np.number])
        if numeric_columns.shape[1] < 2:
            print("⚠️ Not enough numerical columns for correlation analysis. Skipping correlation matrix.")
        else:
            correlation_matrix = numeric_columns.corr()
            correlation_matrix_file = os.path.join(output_folder_path, "correlation_matrix.csv")
            correlation_matrix.to_csv(correlation_matrix_file)
            print(f"✅ Correlation Matrix saved at: {correlation_matrix_file}")
