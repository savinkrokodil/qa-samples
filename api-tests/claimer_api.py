import requests

BASE_URL = "https://mock-api.test"

def create_case(data):
    response = requests.post(f"{BASE_URL}/cases", json=data)
    return response
