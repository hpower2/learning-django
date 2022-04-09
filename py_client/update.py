import json
import requests

endpoint = "http://localhost:8000/api/products/4/update/"

data = {
    'title' : 'World War 2',
    'price' : 12.03,
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())

  