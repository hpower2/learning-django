import json
import requests

endpoint = "http://localhost:8000/api/products/5551661615/"

get_response = requests.get(endpoint)

print(get_response.json())

  