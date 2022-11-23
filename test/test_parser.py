import unittest
from src.parser import Parser
import pandas as pd
from pandas.testing import assert_frame_equal

class TestParser(unittest.TestCase):

    parser = Parser()

    def test_create_union(self):
        '''Tests that the union creates one union of the three different dfs'''
        df1 = pd.DataFrame([['ARID3A', 'ARID3A'],['ARID3A', 'PLA2G15']], columns=['TF', 'Gene'])
        df2 = pd.DataFrame([['ARNT', 'LOX'], ['ARID3A', 'ARID3A']], columns=['TF', 'Gene'])
        df3 = pd.DataFrame([['LOX', 'ARNT']], columns=['TF', 'Gene'])
        df_result = self.parser.create_union([df1, df2, df3])
        df_solution = pd.DataFrame([['ARID3A', 'ARID3A'], ['ARID3A', 'PLA2G15'],
                                    ['ARNT', 'LOX'],['LOX', 'ARNT'] ], columns=['TF', 'Gene'])
        assert_frame_equal(df_result, df_solution)

    def test_write_file(self):
        '''Tests that the output of the functions corresponds to the asked format'''
        pass

    def test_read_in_dataframes(self):
        self.parser.read_in_dataframes(['sw', 'wsw'])


if __name__ == '__main__':
    unittest.main()
