import requests

# Example car specs (order here doesn't matter for JSON, but keys must match training features)
car = {
    "displacement": 140.0,
    "cylinders": 4,
    "horsepower": 90.0,
    "weight": 2264.0,
    "acceleration": 15.5,
    "model_year": 82,
    "origin": 1
}

# Prediction service URL — match the port from predict.py
url = 'http://localhost:9896/predict'

try:
    response = requests.post(url, json=car)
    response.raise_for_status()  # Raise an error for bad responses (4xx/5xx)
    print("Prediction response:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Error calling prediction service: {e}")
