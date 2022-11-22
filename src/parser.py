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
