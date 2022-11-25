from typing import List
import pandas as pd
from src.client import Client
from src.parser import Parser

class GrandParser(Parser):
    client = Client()

    def data_clean(self, dirty_df : pd.DataFrame):
        '''
        Converts the dataframe in needed format

        :param pd.DataFrame dirty_df: the dirty dataframe
        :return: cleaned version of the dataframe
        '''

        #Mapping Ensemble from Gene to GeneSymbol
        list_of_genes_in_ensemble = dirty_df['Gene'].tolist()
        genesymbol_list = self.client.batch_processing_requests(list_of_genes_in_ensemble,'EnsemblGeneId&taxonId=9606',
                                                                'genesymbol')
        clean_df = dirty_df.drop('Gene', axis=1)
        clean_df['Gene'] = genesymbol_list

        return clean_df

    def read_in_dataframes(self, list_of_filenames: List[str], folder_path: str='./'):
        '''
        Reads in all of the dataframes and transforms them into the right format

        :param list list_of_filenames: list of all the different data sets locations
        :param str folder_path: path to all the specific file names
        :return list of dataframes
        '''

        list_dfs = []
        for filename in list_of_filenames:
            list_dfs.append(self.handle_adjacency_matrix(filename))
        return list_dfs

    def handle_adjacency_matrix(self,file_path: str,treshhold: int=2):
        '''
        Reads in a file in the adjacency matrix format and returns df containing genes an TF.
        Needs a treshhold to specify if it is enough evidence for an edge between the genes.

        :param int treshhold: if value above, then it is an edge
        :param str file_path: defines the path to the dataset file
        :return pd.DataFrame: df containing TF and Genes
        '''
        tf_list = []
        gene_list = []
        column_values_genes = []
        #Reads in line per line
        f = open(file_path,'r')
        matrix_in_lines = f.readlines()
        for index, line in enumerate(matrix_in_lines):
            #First line read in
            if index == 0:
                column_values_genes = line.split(',')[1:]
            else:
                weights_of_line = line.split(',')
                tf = weights_of_line[0]

                for i in range(1,len(line.split(','))):
                    if float(weights_of_line[i]) >= treshhold:
                        tf = self.format_string(tf)
                        gene = column_values_genes[i-1]
                        gene = self.format_string(gene)
                        tf_list.append(tf)
                        gene_list.append(gene)

        adj_df = pd.DataFrame({'TF': tf_list, 'Gene': gene_list})
        return adj_df

    def format_string(self, input_string : str):
        '''Deletes unnecessary character

        :param str input_string: the string to format
        :return str: transformed string
        '''

        return input_string.replace('\n','').replace('"','')