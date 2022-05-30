import typer
app = typer.Typer()

@app.command()
def hello():
    print("hello added...")
@app.command()
def check_version(a:int):
    print(f"version checking...{a}")

@app.command()
def add_version():
    print("version added...")

if __name__ == "__main__":
    app()