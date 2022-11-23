from typing import List
import pandas as pd
from src.client import Client
from src.parser import Parser

class HumanBaseParser(Parser):
    client = Client()

    def read_in_dataframes(self, list_of_filenames: List[str], folder_path: str = './'):
        '''Overrides the read in process of the dataframes due to missing header
        Loads all dataframes n a dataframe

        :param list list_of_filenames: list of filenames
        :param folder_path: path of folder containing the datasets
        :return: a list of Panda DataFrame'''
        data_frames = []
        for file in list_of_filenames:
            data = pd.read_csv(folder_path + file, sep='\t', header=None)
            data_frames.append(data)
        return data_frames



    def data_clean(self, dirty_df: pd.DataFrame):
        '''Aligns the HumanBase data format to the needed one

        :param pd.DataFrame dirty_df: the dataframe which needed to be cleaned
        :return pd.DataFrame: a dataframe in the right format
        '''
        cleaned = dirty_df.iloc[:,:2]
        cleaned.columns = ['TF', 'Gene']

        #Conversion to Gene Symbols
        tf_gene_ids_list = cleaned['TF'].values.tolist()
        gene_gene_ids_list = cleaned['Gene'].values.tolist()
        mapped_tf_list = self.client.batch_processing_requests(tf_gene_ids_list, 'geneid', 'genesymbol')
        mapped_gene_list = self.client.batch_processing_requests(gene_gene_ids_list, 'geneid', 'genesymbol')
        dict_mapped_list = {'TF': mapped_tf_list, 'Gene': mapped_gene_list}
        cleaned_dataframe = pd.DataFrame(dict_mapped_list)

        return cleaned_dataframe