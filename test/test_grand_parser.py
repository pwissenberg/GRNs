import unittest
import pandas as pd
from pandas.testing import assert_frame_equal

from src import grand_parser
from src.grand_parser import GrandParser

class TestGrandParser(unittest.TestCase):
    grand_parser = GrandParser()

    def test_data_clean(self):
        pass


