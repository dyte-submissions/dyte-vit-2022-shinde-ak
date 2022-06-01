
import json
from urllib import response
from matplotlib.font_manager import json_dump 
import requests


def get_version(pack,a:str):
    # a="https://github.com/dyte-in/react-sample-app"
    # a = a.replace("https://github.com","https://raw.githubusercontent.com")
    # a = a +"/main/package-lock.json"
    # print(a,"\n")
    # response = requests.get("https://raw.githubusercontent.com/dyte-in/javascript-sample-app/main/package-lock.json")
    # print(a,"\n")
    response = requests.get(a)

    # print("responce from server is :")
    # print(response.status_code)
    # data = response.json()
    data = response.json().get('packages')
    # print(type(data))
    return (data['']['dependencies'][pack])
    # return (data['node_modules/array-flatten']['version'])

# print(get_version("axios","b"))

if __name__=="__main__":
    get_version("a","b")