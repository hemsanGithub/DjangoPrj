import requests
import json

URL = "http://127.0.0.1:8000/studcreate/"

py_data = {
    'name': 'Dilip reddy',
    'roll': 121,
    'city': 'bangalore'
    }

json_data = json.dumps(py_data)

response = requests.post(url=URL, data=json_data)

data = response.json()
print(data)