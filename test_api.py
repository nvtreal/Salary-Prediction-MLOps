import requests

# Ensure the MLflow model server is running on port 5001
url = "http://127.0.0.1:5001/invocations"

# Input data: change the value in the nested list (e.g., [[10.0]]) to test different inputs
input_years = 1
data = {
    "dataframe_split": {
        "columns": ["YearsExperience"], 
        "data": [[input_years]]
    }
}

try:
    response = requests.post(url, json=data)
    response.raise_for_status() # Check for HTTP errors
    
    prediction = response.json()['predictions'][0]
    print(f"Status Code: {response.status_code}")
    print(f"Salary prediction for {input_years} years of experience: ${prediction:,.2f} USD")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the server. Is your MLflow model serve running?")
except Exception as e:
    print(f"An error occurred: {e}")