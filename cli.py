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
from data_pipeline.visual import Visualizer

app = typer.Typer()
download_app = typer.Typer()
client = Client()
parser: (Parser|GrndbParser|GrandParser|HumanBaseParser) = Parser()
visualizer = Visualizer()
input_validator = InputValidator()

@app.command()
def download(input_file: str, output_folder: str = './'):
    '''
    Downloads every dataset from the input file

    :param str input_file: Path to the file; The file contains all urls to download
    :param str output_folder: Optional path to a folder to store all of the datasets.
    '''

    input_validator.check_existence_of_paths([input_file, output_folder])
    return client.download_datasets_from_file(input_file, output_folder)

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
    dataset_list = parser.read_datasets(input_file)
    united_df = parser.create_union(dataset_list)
    parser.write_file(united_df, 'UNITED_dataset.txt', output_folder)

@app.command()
def visualize(input_file: str, statistical_op: str):
    '''
    Plots the degree distribution of the dataset

    :param str input_file: file to the final dataset/GRN
    :param str statistical_op: defines if it should plot the degree distribution of the GRN, the log-transformed degree
    distribution, or only a summary statistics after transforming the

    '''
    input_validator.check_existence_of_paths([input_file])
    input_validator.check_statistics([statistical_op])
    parser = Parser()

    df = parser.read_in_dataframes([input_file])
    edges_degree_list = visualizer.count_edges_per_gene(df[0])
    prepared_df = visualizer.prepare_dataset_for_visulization(edges_degree_list)
    match statistical_op:
        case 'log_plot':
            visualizer.plot_log_number_nodes_log_degree(prepared_df)
        case 'plot':
            visualizer.plot_number_nodes_degrees(prepared_df)
        case 'fitting_summary':
            visualizer.fitting_test(prepared_df)

@app.command()
def complete(input_file: str, input_db: str,output_folder: str = './'):
    '''
    Conducts the whole data pipeline process of downloading, formatting and building the union. !!!Here you can download
    the data sets from one data base. Because in the formatting step you need to know the

    :param input_file: Path to the file; The file contains all urls to download
    :param input_db: Defines the database type for the input
    :param output_folder:
    :return:
    '''
    downloaded_dataset_paths = download(input_file, output_folder)
    #TODO: Find another solution
    f = open('data_sets.txt', 'w')
    f2 = open('cleaned_data_sets.txt', 'w')

    for name in downloaded_dataset_paths:
        f.write(name + '\n')
        f2.write('CLEANED_'+name+'\n')
    f.close()
    format('data_sets.txt',input_db ,output_folder)
    union('cleaned_data_sets.txt',output_folder)

if __name__ == "__main__":
    app()
