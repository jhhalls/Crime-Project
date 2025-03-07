
**download.py**
# 1. Crime Data Retrieval from Kaggle (```python download_data.py```)

This script downloads the “Crime in India” dataset from Kaggle and saves it to a specified local directory. It ensures the directory exists before downloading the dataset.

🚀 How to Use:
1.	Install dependencies: 
```pip install kagglehub```

2.	Set up Kaggle API:
		•	Download kaggle.json from Kaggle (Account Settings > API).
		•	Place it in ~/.kaggle/ (Linux/macOS) or %HOMEPATH%\.kaggle\ (Windows).
3.	Run the script: 
```python download_data.py```

The dataset will be saved in: `./data/raw/raw_data_from_kaggle`


**clean_data.py**  

2. Data Cleaning and Preprocessing (python clean_data.py```)
- The standardize_and_clean function ensures consistent formatting of column names and removes unwanted whitespace in a Pandas DataFrame.
	- 🚀 Function Overview
    	- ✔ Standardizes column names by:
			•	Converting them to lowercase
			•	Replacing spaces with underscores
			•	Removing leading and trailing whitespace
		✔ Cleans all data values by stripping extra spaces.

	### ✅  Function -  `standardize_and_clean` 

	| **Operation**                                  | **Status** |
	|----------------------------------------------|:---------:|
	| Remove leading & trailing whitespace from column names | ✅ |
	| Convert column names to lowercase           | ✅ |
	| Replace spaces in column names with underscores | ✅ |
	| Remove leading & trailing whitespace from all data values | ✅ |
	| Maintain `NaN` values as-is                  | ✅ |

	### ✅ Function -  `remove_duplicates`

	| **Operation**                                | **Status** |
	|---------------------------------------------|:---------:|
	| Identify duplicate rows                     | ✅ |
	| Remove duplicate rows                       | ✅ |
	| Maintain only unique records                | ✅ |
	| Print DataFrame shape before and after removal | ✅ |


Data cleaning is a crucial step before analysis or modeling.

1. Handling Duplicates
	•	Check for duplicates: df.duplicated().sum()
	•	Remove duplicates: df.drop_duplicates(inplace=True)
   
2. Handling Missing Values
	•	Check for missing values: df.isnull().sum()
	•	Drop missing values (if they are insignificant): df.dropna()
	•	Impute missing values
	•	Numeric: Mean/Median (df.fillna(df['column'].mean()))
	•	Categorical: Mode (df.fillna(df['column'].mode()[0]))
	•	Forward/Backward fill: df.fillna(method='ffill') or df.fillna(method='bfill')

3. Fix Data Types
	•	Convert columns to correct data types:
	•	df['date'] = pd.to_datetime(df['date'])
	•	df['price'] = df['price'].astype(float)
	•	Check incorrect types: df.dtypes

4. Handling Outliers
	•	Visualize outliers using boxplots: sns.boxplot(df['column'])
	•	Remove or cap extreme values:
	•	Z-score method (scipy.stats.zscore())
	•	IQR method (df['column'].clip(lower_bound, upper_bound))

5. Standardizing & Formatting Data
	•	Trim spaces: df['column'] = df['column'].str.strip()
	•	Convert text to lowercase: df['column'] = df['column'].str.lower()
	•	Rename columns for consistency: df.rename(columns={'old_name': 'new_name'})

6. Handling Inconsistent Categories
	•	Check unique categories: df['category'].unique()
	•	Standardize category names:
	•	Convert variations to one standard name: df['category'].replace({'Male ': 'Male'})
	•	Use LabelEncoder or OneHotEncoder for categorical encoding if needed

7. Fix Structural Errors
	•	Check for typos in categorical data (e.g., “NY” vs. “New York”)
	•	Merge inconsistent values (df['column'].replace({'N.Y.': 'New York'}))

