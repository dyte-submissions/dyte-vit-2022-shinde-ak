
import json
from urllib import response 
import requests


def get_version(link:str):
    response = requests.get(link)
    print(response.status_code)
    data = response.json()
    return (data['version'])

if __name__=="__main__":
    get_version("a")