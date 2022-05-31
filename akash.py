from struct import pack
from turtle import shape
from importlib_metadata import version
import typer
import numpy as np 
import pandas as pd
import version


app = typer.Typer()



@app.command()
def check_version(a:str,b:str):
    b = b.split('@')
    pack = b[0]
    split_version = b[1].split('.')
    global data 
    data = pd.read_csv(a)
    link= data["repo"]
    version_list = []
    version_satisfied=[]
    for i in range(len(link)):
        modified = modify(link[i])
        fetched = version.get_version(pack,modified)
        version_list.append(fetched)
        version_satisfied.append("true" if validate(split_version,fetched) else "false")
    data["version"] = version_list
    data["version_satisfied"] = version_satisfied
    data.to_csv("output.csv",index=False)
    print("sucessfully fetched and data stored in output.csv file...")
    



@app.command()
def add_version():
    print("adding new version...")

def modify(a:str):
    a= a.replace("https://github.com","https://raw.githubusercontent.com")
    a = a + "/main/package-lock.json"
    return a

def validate(a:list,b:str):
    b= b.replace('^',"")
    fetched = b.split('.')
    if(a[0]>fetched[0]):
        return True
    elif(a[0]<fetched[0]):
        return False
    elif(a[0]==fetched[0]):
        if(a[1]>=fetched[1]):
            if(a[1]>fetched[1]):
                return True
            elif(a[1]==fetched[1]):
                if(a[2]>=fetched[2]):
                    return True
                return False
    return True



if __name__ == "__main__":
    app()