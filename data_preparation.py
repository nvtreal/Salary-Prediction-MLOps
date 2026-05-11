# File name: data_preparation.py

import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_salary_data(file_path):
    """
    Reads and preprocesses data from the specific Capstone project dataset.
    
    Args:
        file_path (str): Path to '2687_capstone_project_dataset_v1_vv6_ahjq7xz.csv'
        
    Returns:
        X_train, X_test, y_train, y_test: Split datasets for model training.
    """
    print(f"[*] Loading dataset from: {file_path}")
    
    # 1. Load the dataset
    df = pd.read_csv(file_path)
    
    # Remove unnecessary index column if it exists (common in exported CSVs)
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    
    # 2. Check and handle Missing Values
    # Based on our analysis, the data is currently clean (0 nulls), 
    # but this step is mandatory for a professional MLOps pipeline.
    null_counts = df.isnull().sum()
    if null_counts.any():
        print("[!] Missing values detected. Performing imputation...")
        df['YearsExperience'] = df['YearsExperience'].fillna(df['YearsExperience'].mean())
        df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
    else:
        print("[+] Dataset is clean with no missing values.")

    # 3. Feature and Target Separation
    # X: Years of Experience (Independent variable)
    # y: Salary (Dependent variable to be predicted)
    X = df[['YearsExperience']] 
    y = df['Salary']            

    # 4. Train/Test Split (80% Train - 20% Test)
    # random_state=42 ensures the split is reproducible every time you run it.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=0.2, 
        random_state=42
    )

    print(f"[+] Preprocessing complete.")
    print(f"    - Total samples: {len(df)}")
    print(f"    - Training set: {X_train.shape[0]} samples")
    print(f"    - Testing set: {X_test.shape[0]} samples")
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # Assuming the data file is located in a 'data/' folder
    DATA_FILE = "2687_capstone_project_dataset_v1_vv6_ahjq7xz.csv"
    
    try:
        X_train, X_test, y_train, y_test = prepare_salary_data(DATA_FILE)
        print("\n--- Sample from Training Set ---")
        print(X_train.head())
    except FileNotFoundError:
        print(f"❌ Error: File not found at {DATA_FILE}. Please check the path.")