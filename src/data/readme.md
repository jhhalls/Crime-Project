
**download.py**
# 1. Crime Data Retrieval from Kaggle (```python download_data.py```)

### ✅ Function 

| **Operation**                                      | **Status** |
|---------------------------------------------------|:---------:|
| Define the local directory path                  | ✅ |
| Check if the directory exists                    | ✅ |
| Create the directory if it doesn't exist         | ✅ |
| Print directory creation confirmation            | ✅ |
| Download the dataset from Kaggle                 | ✅ |
| Save the dataset to the specified local path     | ✅ |
| Print dataset download confirmation              | ✅ |



**clean_data.py**  

2. Data Cleaning and Preprocessing (```python clean_data.py```)

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

