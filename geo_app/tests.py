from django.test import TestCase
import requests
import json

def street_search_req(city):
    data ={
    "city": city
    }
    headers = {'Content-type': 'application/json'}
    req = requests.post("http://127.0.0.1:8000/street/", data=json.dumps(data), headers=headers)
    return req.text


for i in range(10000):
    print(street_search_req('Bolimów'))