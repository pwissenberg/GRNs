import unittest
import os
import pandas as pd
from pandas.testing import assert_frame_equal
from src.grand_parser import GrandParser

class TestGrandParser(unittest.TestCase):
    grand_parser = GrandParser()

    def test_data_clean(self):
        '''Test the cleaning of the data process'''
        #Create the input to test
        df_input = pd.DataFrame([['AHR', 'ENSG00000000419'],
                               ['AHR', 'ENSG00000000460'],
                               ['ARNT', 'ENSG00000000005'],
                               ['ARNT', 'ENSG00000000457'],
                               ['ARNT', 'ENSG00000000460']], columns=['TF', 'Gene'])
        df_solution = pd.DataFrame([['AHR', 'DPM1'],
                               ['AHR', 'C1orf112'],
                               ['ARNT', 'TNMD'],
                               ['ARNT', 'SCYL3'],
                               ['ARNT', 'C1orf112']], columns=['TF', 'Gene'])
        df_result = self.grand_parser.data_clean(df_input)
        assert_frame_equal(df_result, df_solution)

    def test_handle_adjacency_matrix(self):
        '''Testing the adjacency matrix formating'''
        test = os.getcwd()
        df_result = self.grand_parser.handle_adjacency_matrix('test_adjacency_matrix.txt')
        df_sol = pd.DataFrame([['AHR','ENSG00000000419'],
                               ['AHR','ENSG00000000460'],
                               ['ARNT','ENSG00000000005'],
                               ['ARNT','ENSG00000000457'],
                               ['ARNT','ENSG00000000460']], columns=['TF','Gene'])
        assert_frame_equal(df_result, df_sol)