import pandas as pd

from src.parser import Parser

class GrndbParser(Parser):

    def __init__(self):
        pass

    def data_clean(self, dirty_df: pd.DataFrame):
        '''We only take the edges with labeled as Confidence High

        :param pd.DataFrame dirty_df: the dataframe which needed to be cleaned
        :return pd.DataFrame: a dataframe in the right format'''
        data = dirty_df[dirty_df['Confidence'] == 'High']
        data = data[['TF', 'gene']].copy()
        data = data.rename(columns={'gene':'Gene'})
        data.reset_index(drop=True, inplace=True)
        return data