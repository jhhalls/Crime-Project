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

8.  Normalize & Scale Data (if required for ML)
	•	Apply Min-Max Scaling or Standardization for numerical features:

from sklearn.preprocessing import MinMaxScaler, StandardScaler
scaler = MinMaxScaler()
df[['column']] = scaler.fit_transform(df[['column']])

