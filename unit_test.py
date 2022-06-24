import unittest
import pandas as pd
import os


class TestCases(unittest.TestCase):
    def test_shape(self):
        self.df_main = pd.read_csv(os.path.join(os.path.abspath(os.curdir)+'/main_data' +'/df_main.csv'))
        self.assertAlmostEqual(self.df_main.shape[0], 18)
        self.assertAlmostEqual(self.df_main.shape[1], 9)





?//////////////////////////////////

To Run the File use the bellow command:

python -m unittest unit_test.py

