import requests
from utils.config import app_config

base_url = app_config["api_url"]

def test_health():
    health_api_endpoint = f"{base_url}/health"
    response = requests.get(health_api_endpoint)
    return response.json()

# op = test_health()
# print(op)
