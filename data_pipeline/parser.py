from typing import List

import pandas as pd
class Parser(object):

    def __init__(self):
        pass

    def read_datasets(self, file_path: str):
        '''
        The file stores all the different paths to the datasets. The function reads in all datasets

        :param str file_path: path to the input-file
        :return list[str]: list of paths to the single databases
        '''

        names_of_datasets = []
        with open(file_path, 'r') as read:
            for index, line in enumerate(read):
                names_of_datasets.append(line.replace('\n',''))
        return names_of_datasets

    def create_union(self, dataset_list: []):
        '''
        Creates the union of a list of dataframes by dropping duplicates

        :param list[str] dataset_list: list of cleaned dataframes
        return pandas.DataFrame: the created union between the DataFrame list
        '''

        df = pd.concat(dataset_list)
        df.drop_duplicates(keep='first', inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df

    def write_file(self, dataframe: pd.DataFrame,filename: str, output_file_path: str='./'):
        '''
        Writes the dataframe to the output path

        :param pandas.DataFrame dataframe: DataFrame to write as a file
        :param str filename: Defines the filename of the output file
        :param str output_file_path: Optional path to store the output_file at a differetn location
        '''
        dataframe.to_csv(output_file_path+filename, sep='\t', index=False, header=True)

    def write_all_files(self, dataframes: list[pd.DataFrame],filename_list: list[str], output_file_path:str = './'):
        '''
        Writes all of the dataframes into their respective files

        :param list[pandas.dataframe] dataframes: list of dfs which are going to be stored
        :param list[str] filename_list: list of the given filenames
        :param str output_file_path: Optional path to store the datasets at a different location
        '''

        for index, df in enumerate(dataframes):
            self.write_file(df,filename_list[index], output_file_path)

    def read_in_dataframes(self, list_of_filenames: List[str], folder_path: str='./'):
        '''
        Loads all dataframes and returns them in a list

        :param list[str] list_of_filenames: list of filenames
        :param str folder_path: path of folder containing the datasets
        :return list[pandas.DataFrame]: a list of Panda DataFrames
        '''

        data_frames = []
        for file in list_of_filenames:
            data = pd.read_csv(folder_path + file, sep='\t')
            data_frames.append(data)
        return data_frames

    def data_clean(self, dirty_df : pd.DataFrame):
        '''
        The data cleaning process has to be conducted for each dataframe, which provides a different data format

        :param pandas.DataFrame dirty_df: the dataframe to clean
        :return pandas.DataFrame: a cleaned dataframe with the right format
        '''

        raise NotImplementedError('Please implenent the data cleaning process for each database!')

    def clean_all_data(self, dirty_dfs: List[pd.DataFrame]):
        '''
        Conducts the data cleaning process for all datasets
        :param list[pandas.DataFrame] dirty_dfs: list of the dirty dataframes
        :return list[str]: a list of cleaned dataframes
        '''

        clean_dfs = []
        for df_dirty in dirty_dfs:
            cleaned_df = self.data_clean(df_dirty)
            clean_dfs.append(cleaned_df)
        return clean_dfs

    def get_all_filenames(self, list_of_paths: list[str]):
        '''
        Gets the paths and returns the name of the files

        :param list_of_paths: file containing all the paths to the datasets
        :return list[str]: return a list of the filenames
        '''
        filenames = []
        for path in list_of_paths:
            filenames.append('CLEANED_' + path.split('/')[-1])
        return filenames