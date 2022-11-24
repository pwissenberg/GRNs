import typer
from .parser import Parser
from .client import Client
app = typer.Typer()
download_app = typer.Typer()
client = Client()
parser = Parser()

@app.command()
def download(input: str, output_folder: str = './'):
    '''Downloads every dataset from the input file

    :param str input: Path to the file. Containing all f the links.
    :param str output: Optional path to a folder to store all of the datasets.
    '''
    client.download_datasets_from_file(input, output_folder)

@app.command()
def concat():
    pass

@app.command()
def complete_data_pip():
    pass


if __name__ == "__main__":
    app()
