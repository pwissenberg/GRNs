import unittest
import pandas as pd
from data_pipeline.visual import Visualizer

class TestCli(unittest.TestCase):
    visulizer = Visualizer()

    def test_count_edges_per_gene(self):
        '''
        Tests th counting of each gene
        '''
        #df_input = pd.DataFrame([['ARID3A', 'ARID3A'],['ARID3A', 'PLA2G15'], ['ARNT', 'LOX'], ['LOX','ARNT']], columns=['TF', 'Gene'])
        sol_list = [3,2,2,1]
        df_input = pd.read_csv('../final_GRN.txt', sep='\t')
        #Call the function
        result_list = self.visulizer.count_edges_per_gene(df_input)
        result_df = self.visulizer.prepare_dataset_for_visulization(result_list)
        #self.visulizer.plot_number_nodes_degrees(result_df)
        #self.visulizer.plot_log_number_nodes_log_degree(result_df)
        self.visulizer.fitting_test(result_df)
        #self.visulizer.plot_log_number_nodes_log_degree(result_df)
        #self.assertListEqual(result_list, sol_list)

    def test_plot_degree_distribution(self):
        '''
        Tests that the degree distribution graph is created
        '''
        self.visulizer.plot_number_nodes_degrees([12, 42, 5, 5, 6, 677])
        pass
    def test_plot_histo(self):
        df_input = pd.read_csv('../final_GRN.txt', sep='\t')
        self.visulizer.plot_histo(df_input)

