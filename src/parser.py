from typing import List

import pandas as pd
class Parser(object):

    def __init__(self):
        pass

    def read_dataset(file_path: str):
        '''The file stores all the different paths to the datasets. The function reads in all datasets.'''
        names_of_datasets = []
        with open(file_path, 'r') as read:
            for index, line in enumerate(read):
                pass

    def create_union(self, dataset_list: []):
        '''Creates the union of a list of dataframes by dropping duplicates'''
        df = pd.concat(dataset_list)
        df.drop_duplicates(keep='first', inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df

    def write_file(self, dataframe: pd.DataFrame, output_file_path: str):
        '''Writes the dataframe to the output path'''
        dataframe.to_csv(output_file_path, sep='\t', index=False, header=True)

    def read_in_dataframes(self, list_of_filenames: List[str], folder_path: str='./'):
        '''Loads all dataframes and returns them in a list

        :param list list_of_filenames: list of filenames
        :param folder_path: path of folder containing the datasets
        :return: a list of Panda DataFrames'''
        data_frames = []
        for file in list_of_filenames:
            data = pd.read_csv(folder_path + file, sep='\t')
            data_frames.append(data)
        return data_frames

    def data_clean(self, dirty_df : pd.DataFrame):
        '''The data cleaning process has to be conducted for each dataframe, which provides a different data format

        :param pd.DataFrame dirty_df: the dataframe to clean
        :return: a cleaned dataframe with the right format
        '''

        raise NotImplementedError('Please implenent the data cleaning process for each database!')

    def clean_all_data(self, dirty_dfs: List[pd.DataFrame]):
        '''Conducts the data cleaning process for all datasets
        :param List dirty_dfs: list of the dirty dataframes
        :return: a list of cleaned dataframes'''
        clean_dfs = []
        for df_dirty in dirty_dfs:
            cleaned_df = self.data_clean(df_dirty)
            clean_dfs.append(cleaned_df)
        return clean_dfs