import requests

endpoint = "http://127.0.0.1:8000/api/products/"


get_response = requests.post(
    endpoint,
    json={
        "title": "im hereamsdmaskke",
        "content": "test4",
        "price": "1.22",
    },
)  # API
print(get_response.json())
