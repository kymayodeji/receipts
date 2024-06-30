## Sample Python File for calling an API to process requests
import json
import requests

# Processing the JSON response
def get_features(json_response):
    parsed_data = {}    
    prediction = json_response["predictions"][0]    
    parsed_data["total_amount"] = prediction["total"]["amount"]
    parsed_data["time"] = prediction["time"]["iso"]
    parsed_data["date"] = prediction["date"]["iso"]
    parsed_data["category"] = prediction["category"]["value"]
    return parsed_data

# API URL
url = "https://api.mindee.net/v1/products/mindee/expense_receipts/v5/predict"
my_api_key = "aa9fb5fc22ba800e856a5c3ae20892ad"
image_path = "data/aldi2024.png"

with open(image_path, "rb") as image_file:
    files = {"document": image_file}
    headers = {"Authorization": f"Token {my_api_key}"}
    response = requests.post(
        url,
        headers=headers,
        files=files,
    )
    if response.status_code != 200:
        print("Request error")
    else:
        json_response = response.json()
        features = get_features(json_response)
        print("Date:", features["date"])
        print("Time:", features["time"])
        print("Total amount:", features["total_amount"])
        print("Category:", features["category"])
    
