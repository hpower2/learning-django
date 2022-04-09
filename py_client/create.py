import json
import requests

headers = {
    'Authorization' : 'Bearer a2ab1d1c8d361274c3d0d39802b7efbc961fab6d'
}

endpoint = "http://localhost:8000/api/products/"

data = {
    'title': 'Myname is irvine',
    'price' : 27.99
    }
get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())

