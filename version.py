
import json
from urllib import response 
import requests


def get_version(a:str):
    # a="https://github.com/dyte-in/react-sample-app"
    # a = a.replace("https://github.com","https://raw.githubusercontent.com")
    # a = a +"/main/package-lock.json"
    # print(a,"\n")
    # response = requests.get("https://raw.githubusercontent.com/dyte-in/javascript-sample-app/main/package-lock.json")
    print(a,"\n")
    response = requests.get(a)

    print("responce from server is :")
    print(response.status_code)
    data = response.json()
    print("version fetched is :",data['version'] )
    return (data['version'])

if __name__=="__main__":
    get_version("a")