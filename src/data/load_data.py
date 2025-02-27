import os
import pandas as pd
from src.utils.logger import get_logger  # ✅ Ensure correct import

# Initialize logger
logger = get_logger(__name__)
# Dictionaries to store DataFrames and track file processing status
dataframes = {}
successful_files = []
problematic_files = []
file_issues = {}  # Store issues per file

def load_csv_files(csv_directory, expected_columns=22):
    """
    Reads all CSV files in a given directory, detects problematic lines with issue tags,
    handles errors, and returns a dictionary of DataFrames along with access instructions.

    Parameters:
        csv_directory (str): Path to the directory containing CSV files.
        expected_columns (int): Expected number of columns in each CSV file.

    Returns:
        tuple: (dataframes, access_instructions)
            - dataframes (dict): Dictionary of successfully loaded DataFrames.
            - access_instructions (str): Instructions on how to access the DataFrames.
    """

    # List all CSV files in the directory
    try:
        csv_files = [f for f in os.listdir(csv_directory) if f.endswith(".csv")]
        if not csv_files:
            logger.warning(f"No CSV files found in {csv_directory}")
            return {}, "No CSV files found."

    except FileNotFoundError:
        logger.error(f"Directory not found: {csv_directory}")
        return {}, "Directory not found."



    logger.info(f"📂 Found {len(csv_files)} CSV files in directory: {csv_directory}")

    for file in csv_files:
        file_path = os.path.join(csv_directory, file)
        df_name = os.path.splitext(file)[0]  # Filename without extension
        
        logger.info(f"🔍 Processing file: {file}")

        has_issue = False  # Track if this file has any issues
        issues = []  # Store line-specific issues

        # Step 1: Detect problematic lines before reading
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    column_count = line.count(",") + 1  # Columns = commas + 1

                    if column_count > expected_columns:
                        issue_tag = "⚠️ Extra Columns"
                    elif column_count < expected_columns:
                        issue_tag = "⚠️ Missing Columns"
                    else:
                        continue  # Skip lines without issues

                    issues.append(f"Line {i}: {issue_tag} → {line.strip()}")
                    has_issue = True
        except Exception as e:
            logger.error(f"Error reading file {file}: {e}")
            problematic_files.append(file)
            continue

        # Step 2: Try reading the CSV file
        try:
            df = pd.read_csv(file_path, on_bad_lines="skip")  # Skip bad lines
            dataframes[df_name] = df
            logger.info(f"✅ Successfully loaded {file} into DataFrame '{df_name}'")
            successful_files.append(file)
        except pd.errors.ParserError as e:
            logger.error(f"❌ Error reading {file}: {e}")
            has_issue = True

        # Step 3: Track problematic files
        if has_issue:
            problematic_files.append(file)
            file_issues[file] = issues  # Store line-specific issues

    # Print final summary
    logger.info("\n📌 **Processing Summary:**")
    logger.info(f"✅ Successfully Processed Files ({len(successful_files)}):")

    for file in successful_files:
        logger.info(f"   - {file}")

    if problematic_files:
        logger.warning(f"\n⚠️  Problematic Files ({len(problematic_files)}):")
        for file in problematic_files:
            logger.warning(f"   - {file}")

        # Print detailed issue report
        logger.warning("\n📌 **Detailed Issue Report:**")

        for file, issues in file_issues.items():
            logger.warning(f"\n🔍 Issues in {file}:")
            for issue in issues:
                logger.warning(f"   {issue}")

    else:
        logger.info("\n✅ No issues detected in any files!")

    logger.info("\n🚀 DataFrames created: " + str(list(dataframes.keys())))

    # Generate access instructions
    access_instructions = "\n🔹 **How to Access the DataFrames:**\n"
    access_instructions += "Use the following commands to access individual DataFrames:\n"
    
    for df_name in dataframes.keys():
        access_instructions += f"  👉 `dataframes['{df_name}'].head()`  # View first 5 rows of {df_name}.csv\n"

    if problematic_files:
        logger.warning("Data loaded with issues. Please check the detailed issue report.")
    else:
        logger.info("Data loaded successfully.")
    # Return DataFrames and instructions
    return dataframes, access_instructions