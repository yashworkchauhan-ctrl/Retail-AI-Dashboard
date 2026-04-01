import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "Quantity": 5,
    "Discount": 0.1
}

response = requests.post(url, json=data)

print(response.json())