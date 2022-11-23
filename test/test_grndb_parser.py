import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from src.grndb_parser import GrndbParser

class TestGrndbParser(unittest.TestCase):
    grndbParser = GrndbParser()

    def test_data_clean(self):
        '''Testing the data cleaning of one dataframe'''
        #Create a dataframe to clean
        dirty_df = pd.DataFrame([['ARID3A','PLA2G15','hocomoco__ARI3A_HUMAN.H11MO.0.D','3.74','0.0159549296676993','High'],
                            ['ARNT','SCARB2','transfac_pro__M04720','3.84','0.0070831231646842595','Low']],
                           columns=['TF','gene','bestMotif','NES','Genie3Weight','Confidence'])
        cleaned_df = self.grndbParser.data_clean(dirty_df)
        clean_df = pd.DataFrame([['ARID3A','PLA2G15']], columns=['TF', 'Gene'])
        assert_frame_equal(cleaned_df,clean_df)


if __name__ == '__main__':
    unittest.main()