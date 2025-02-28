
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Install necessary libraries if not already installed
# !pip install pandas matplotlib seaborn

# Load the dataset (replace 'your_dataset.csv' with the actual file name)
try:
    df = pd.read_csv('/content/Exhaustive Analysis of Indian Agriculture.csv')
except FileNotFoundError:
    print("Error: 'your_dataset.csv' not found. Please upload your dataset or provide the correct file name.")
    exit()

# Display basic information about the dataset
print(df.info())
print(df.describe())

# Explore relationships between variables (replace 'variable1', 'variable2' etc.)
# Numerical variables
numerical_cols = df.select_dtypes(include=['number']).columns
for col1 in numerical_cols:
    for col2 in numerical_cols:
        if col1 != col2:
            plt.figure(figsize=(8, 6))
            sns.scatterplot(x=col1, y=col2, data=df)
            plt.title(f'Scatter plot of {col1} vs. {col2}')
            plt.show()


# Categorical variables (replace 'categorical_variable' with actual variable names)
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    plt.figure(figsize=(10, 6))
    df[col].value_counts().plot(kind='bar')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()


# Correlation analysis for numerical features
correlation_matrix = df[numerical_cols].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# Example analysis: Crop yield vs. rainfall
if 'Crop_Yield' in df.columns and 'Rainfall' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.regplot(x='Rainfall', y='Crop_Yield', data=df)
    plt.title('Crop Yield vs. Rainfall')
    plt.show()


# Further analysis can be performed based on specific questions
# Example: Group by region and calculate average yield
if 'Region' in df.columns and 'Crop_Yield' in df.columns:
    average_yield_by_region = df.groupby('Region')['Crop_Yield'].mean()
    print("Average yield by region:\n", average_yield_by_region)


print("Analysis complete.")
