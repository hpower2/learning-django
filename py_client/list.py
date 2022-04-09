import json
import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/"
username = input("what is your username? \n")
password = getpass("what is your Password? \n")

auth_response = requests.post(endpoint, json={
    "username" : username,
    "password" : password
})

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"
    get_response = requests.get(endpoint, headers=headers)
    data = get_response.json()
    next_url = data['next']
    results = data['results']
    print(next_url)
    print(results)
    # if next_url is not None:
        # get_response = requests.get(next_url, headers=headers)
