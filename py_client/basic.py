import json
import requests

endpoint = "http://localhost:8000/api/products/create/"

data = {
    'title': 'Myname is irvine',
    # 'content': 'There much to be done',
    'price' : 27.99
    }
get_response = requests.post(endpoint, json=data)

# print(get_response.headers)
# print(get_response.text)
print(get_response.json())
# print(get_response.status_code)
