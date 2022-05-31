from turtle import shape
from importlib_metadata import version
import typer
import numpy as np 
import pandas as pd
import version


app = typer.Typer()



@app.command()
def check_version(a:str,b:str):
    split_version = b.split('.')
    data =pd.read_csv(a)
    link= data["repo"]
    for i in range(link.shape[0]):
        modified = modify(link[i])
        fetched = version.get_version(modified)
        data["version"] = fetched
        data["version_satisfied"] = "true" if validate(split_version,fetched) else "false" 
    pd.to_csv("output.csv")
    print("sucessfully fetched and data stored in output.csv file...")
    


@app.command()
def add_version():
    print("adding new version...")

def modify(a:str):
    a.replace("https://github.com","https://raw.githubusercontent.com")
    a +="/main/package-lock.jsonn"
    return a

def validate(a:list,b:str):
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