import typer

app = typer.Typer()

@app.command()
def download():
    #Create client
    pass



@app.command()
def lol():
    print('sqws')

if __name__ == "__main__":
    app()
