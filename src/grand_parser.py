from typing import List

import pandas as pd

from src.parser import Parser


class GrandParser(Parser):

    def data_clean(self, dirty_df : pd.DataFramef):
        #Mapping Ensemble to
        pass

def read_in_dataframes(self, list_of_filenames: List[str], folder_path: str='./'):
    pass

def handle_adjacency_matrix(self,file_path: str,treshhold: int=2):
    '''Reads in a file in the adjacency matrix format and returns df containing genes an TF.
    Needs a treshhold to specify if it is enough evidence for an edge between the genes.

    :param int treshhold: if value above, then it is an edge
    :param str file_path: defines the path to the dataset file
    :return pd.DataFrame: df containing TF and Genes
    '''
    dict_tf_genes = {'TF': [], 'Gene': []}
    column_values_genes = []
    #Reads in line per line
    f = open(file_path,'r')
    matrix_in_lines = f.readlines()
    for index, line in enumerate(matrix_in_lines):
        #First line read in
        if index == 0:
            column_values_genes = line.split(',')

        #Split the line
        weights_of_line = line.split(',')
        tf = weights_of_line[0]
        for i in range(1,len(line.split(','))):
            if weights_of_line[i] >= treshhold:
                dict_tf_genes.get('TF').append(tf)
                dict_tf_genes.get('Gene').append(weights_of_line[i])
        #Create the dataframe
        adj_df = pd.DataFrame(dict_tf_genes)
        return adj_df