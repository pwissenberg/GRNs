import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from src.humanbase_parser import HumanBaseParser

class TestGrndbParser(unittest.TestCase):
    humanbaseParser = HumanBaseParser()

    def test_data_clean(self):
        '''Testing the data cleaning of one dataframe'''
        #Create a dataframe to clean
        dirty_df = pd.DataFrame([['1820','1820'],['1820','23659']])
        cleaned_df = self.humanbaseParser.data_clean(dirty_df=dirty_df)
        clean_df = pd.DataFrame([['ARID3A','ARID3A'],['ARID3A','PLA2G15']], columns=['TF', 'Gene'])
        assert_frame_equal(cleaned_df,clean_df)

if __name__ == '__main__':
    unittest.main()