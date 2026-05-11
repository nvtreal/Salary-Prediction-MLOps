# File name: tests/test_pipeline.py
import pytest
import pandas as pd
import os
import sys

# Add the root directory to path so we can import our modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_preparation import prepare_salary_data

TEST_DATA_FILE = "test_data_dummy.csv"

@pytest.fixture
def create_dummy_data():
    """Generates a small dummy CSV to test the pipeline logic quickly"""
    df = pd.DataFrame({
        'YearsExperience': [1.1, 2.0, 3.2, 4.0, 5.5, 6.8, 7.1, 8.9, 9.5, 10.3],
        'Salary': [39000, 43000, 54000, 63000, 81000, 91000, 98000, 109000, 116000, 122000]
    })
    df.to_csv(TEST_DATA_FILE, index=False)
    yield TEST_DATA_FILE
    if os.path.exists(TEST_DATA_FILE):
        os.remove(TEST_DATA_FILE)

def test_data_preparation(create_dummy_data):
    """Verifies that the 80/20 split works and no data is lost/null"""
    X_train, X_test, y_train, y_test = prepare_salary_data(create_dummy_data)
    
    # Check split logic (10 rows -> 8 Train, 2 Test)
    assert len(X_train) == 8, "Training set should have 8 samples"
    assert len(X_test) == 2, "Test set should have 2 samples"
    
    # Ensure no Null values were introduced
    assert X_train.isnull().sum().sum() == 0, "Training data contains Null values"
    assert X_test.isnull().sum().sum() == 0, "Test data contains Null values"