import requests

endpoint = "http://127.0.0.1:8000/api/products/3/update/"


get_response = requests.put(
    endpoint,
    json={
        "title": "testing the update",
    },
)  # API
print(get_response.json())
