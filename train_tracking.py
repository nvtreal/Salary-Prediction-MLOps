import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Setup MLflow Tracking Connection
# Connects to the UI running at localhost:5000
mlflow.set_tracking_uri("http://localhost:5000")

experiment_name = "Salary_Prediction_Capstone"
# Ensure the experiment exists to avoid 'NoneType' errors
experiment = mlflow.get_experiment_by_name(experiment_name)
if experiment is None:
    mlflow.create_experiment(experiment_name)
mlflow.set_experiment(experiment_name)

# 2. Load Real Capstone Dataset
data_path = '2687_capstone_project_dataset_v1_vv6_ahjq7xz.csv'
df = pd.read_csv(data_path)

# Data Preprocessing: 
# Using 'YearsExperience' as the feature (X) and 'Salary' as the target (y)
X = df[['YearsExperience']]
y = df['Salary']

# Split Data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Define the 3 Models for your Checklist
models = [
    ("Linear Regression", LinearRegression()),
    ("Decision Tree", DecisionTreeRegressor(max_depth=5, random_state=42)),
    ("Random Forest", RandomForestRegressor(n_estimators=100, random_state=42))
]

print(f"🚀 Starting training with real data from: {data_path}")

for model_name, model_obj in models:
    # Start a new MLflow run for each model
    with mlflow.start_run(run_name=model_name):
        # Model Training
        model_obj.fit(X_train, y_train)
        predictions = model_obj.predict(X_test)
        
        # Calculate RMSE and R2 metrics
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        r2 = r2_score(y_test, predictions)
        
        # Log Parameters (helps distinguish models in the UI)
        mlflow.log_param("model_type", model_name)
        if "Decision Tree" in model_name or "Random Forest" in model_name:
            mlflow.log_param("random_state", 42)
        
        # Log Metrics (RMSE and R2)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        
        # Log Model Artifact (allows you to Register the model later)
        mlflow.sklearn.log_model(model_obj, "model")
        
        print(f"✅ Finished {model_name:20} | RMSE: {rmse:10.2f} | R2: {r2:.4f}")

print("\n--- TRACKING PROCESS COMPLETE ---")
print("1. Go back to your MLflow UI at localhost:5000.")
print("2. Refresh the page to see the 3 new runs with high R2 scores.")
print("3. Identify the best model and click 'Register Model'.")