from turtle import shape
from importlib_metadata import version
import typer
import numpy as np 
import pandas as pd


app = typer.Typer()

@app.command()
def hello():
    print("hello added...")

@app.command()
def check_version(a:str,b:str):
    split_version = b.split('.')
    data =pd.read_csv(a)
    link= data["repo"]
    for i in range(link.shape[0]):
        data["version"] = version(link[i])
        data["version_satisfied"] = "true" if validate(version(link[i])) else "false" 


    print(f"version checking...{a}")

@app.command()
def add_version():
    print("added")

def version(a:str):
    pass

def validate():
    pass
if __name__ == "__main__":
    app()