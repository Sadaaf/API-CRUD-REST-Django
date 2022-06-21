import requests
import json

response = requests.get('http://127.0.0.1:8000/users')

print(response.json())
for data in response.json()['users']:
    print(data['state_address'])
    print()