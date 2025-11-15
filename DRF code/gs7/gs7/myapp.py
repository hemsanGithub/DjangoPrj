import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    header = {'content-Type': 'application/json'}
    resp = requests.get(url=URL, headers=header, data=json_data)
    data = resp.json()
    print(data)

# get_data()

def post_data():
    data = {
        'name': 'mohit',
        'roll': 16,
        'city': 'hyderabad'
    }
    header = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    resp = requests.post(url=URL, headers=header,data=json_data)
    data = resp.json()
    print(data)

# post_data()

def update_data():
    data = {
        'id': 4,
        'name': 'Rohit',
        'roll': 10,
        'city': 'Pune'
    }
    json_data = json.dumps(data)
    header = {'content-Type': 'application/json'}
    resp = requests.put(url=URL, headers=header, data=json_data)
    data = resp.json()
    print(data)

# update_data()

def delete_data():
    data = {'id': 4}
    json_data = json.dumps(data)
    header = {'content-Type': 'application/json'}
    resp = requests.delete(url=URL, headers=header, data=json_data)
    data = resp.json()
    print(data)

# delete_data()
