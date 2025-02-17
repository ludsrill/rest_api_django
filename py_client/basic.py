import requests

endpoint = "http://127.0.0.1:8000/api"


get_response = requests.post(endpoint, json={"query": "Hello world"})  # API
print(get_response.json())
