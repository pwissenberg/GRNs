import typer
from rich import print
import os
from data_pipeline.client import Client
from data_pipeline.parser import Parser
from data_pipeline.grand_parser import GrandParser
from data_pipeline.grndb_parser import GrndbParser
import pandas as pd
from data_pipeline.humanbase_parser import HumanBaseParser
from data_pipeline.input_validator import InputValidator

app = typer.Typer()
download_app = typer.Typer()
client = Client()
parser: (Parser|GrndbParser|GrandParser|HumanBaseParser) = Parser()
input_validator = InputValidator()

@app.command()
def download(input_file: str, output_folder: str = './'):
    '''
    Downloads every dataset from the input file

    :param str input: Path to the file. Containing all f the links.
    :param str output: Optional path to a folder to store all of the datasets.
    '''

    input_validator.check_existence_of_paths([input_file, output_folder])
    client.download_datasets_from_file(input_file, output_folder)

@app.command()
def format(input_file: str, input_db: str,output_folder: str = './'):
    '''
    Takes the input files and formats the into the required format

    :param str input_file: Path to the file, which contains the paths
    :param str input_db: Defines the database type for the input
    :param str output_folder: Optional path to a folder to store all of the foramted files
    '''

    input_validator.check_existence_of_paths([input_file, output_folder])
    input_validator.check_database([input_db])

    parser = input_validator.create_parser(input_db)
    paths_input_list = parser.read_datasets(input_file)
    filenames_list = parser.get_all_filenames(paths_input_list)
    uncleaned_dfs = parser.read_in_dataframes(paths_input_list)
    cleaned_dfs = parser.clean_all_data(uncleaned_dfs)

    parser.write_all_files(cleaned_dfs, filenames_list, output_folder)

@app.command()
def union(input_file: str, output_folder: str = './'):
    '''
    Creates the union all of the input files to one data set

    :param str input_file: has a list to all the input files
    :param str output_folder: Optional location to store the final data set
    '''
    input_validator.check_existence_of_paths([input_file, output_folder])
    parser = Parser()
    dataset_list = parser.read_datasets()
    united_df = parser.create_union(dataset_list)
    parser.write_file(united_df, 'UNITED_dataset.txt', output_folder)

@app.command()
def visulize():
    #Input finished parsed data set
    #Creates the visualization
    #Stores the visualization
    pass

@app.command()
def complete_data_pip(input_file: str, input_db: str,output_folder: str = './'):

    #Downloads the datasets
    #Format the datasets
    #Union the datasets

    pass


if __name__ == "__main__":
    app()
