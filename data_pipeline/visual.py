import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
class Visualizer(object):

    def count_edges_per_gene(self, df: pd.DataFrame):
        '''
        Calculates the degree of each node in the network

        :param pandas.DataFrame df: the GRN in the righjt format of the pipeline
        :return list[str]: list of all the occurences
        '''

        final_occurences = []
        gene_occurence_series = df['Gene'].value_counts()
        tf_occurence_series = df['TF'].value_counts()

        for gene, occurence in tf_occurence_series.items():
            occuence_in_gene_series = gene_occurence_series.get(gene)
            if occuence_in_gene_series == None:
                final_occurences.append(occurence)
            else:
                final_occurences.append(occurence+occuence_in_gene_series)
                gene_occurence_series.drop(gene, inplace=True)

        for gene, occurence in gene_occurence_series.items():
            final_occurences.append(occurence)
        return final_occurences

    def plot_number_nodes_degrees(self, df_plot: pd.DataFrame):
        '''
        Plots the degree distribtuion of genes/nodes

        :param pandas.DataFrame df_plot: dataframe ordered with the columns degree & counts
        '''
        fig, axe = plt.subplots(figsize=(10,6))
        axe.bar(df_plot['degree'], df_plot['counts'], color = 'blue', width= 1)
        axe.set_title('Plot: number of nodes vs degree of node')
        axe.set_ylabel('Count of nodes with degree')
        axe.set_xlabel('Degree of a node')
        plt.xlim(left=1)
        plt.show()

    def plot_log_number_nodes_log_degree(self, df_plot: pd.DataFrame):
        '''
        Conducts the loglog Transformation and returns the same plot

        :param pandas.DataFrame df_plot: dataframe ordered with the columns degree & counts
        '''
        log_counts = np.log(df_plot['counts'])
        log_degree = np.log(df_plot['degree'])

        fig, a = plt.subplots(figsize=(10,6))
        a.scatter(log_degree, log_counts, s= 1, color='blue')
        a.set_title('$log(counts)=f(logDegree)$')
        a.set_xlabel('logDegree')
        a.set_ylabel('logCount')
        plt.show()

    def prepare_dataset_for_visulization(self, occurence_list: list[int]):
        '''
        Preprocesses the list and creates a dataframe for the visulization

        :param occurence_list: list[int]: parese the list in the right dataframe
        :return pandas.DataFrame: returns the processed dataset
        '''

        degree_dict = {}
        for occurence in occurence_list:
            degree_dict[occurence] = degree_dict.get(occurence, 0) + 1
        print(degree_dict)
        df_plot = pd.DataFrame(degree_dict.items(), columns=['degree', 'counts'])
        df_plot.sort_values(by='degree', ascending=True, inplace=True)
        df_plot.reset_index(drop=True)
        return df_plot

    def fitting_test(self,df: pd.DataFrame):
        '''
        Gives a basic summary statistics to check
        :param pandas.DataFrame df: input dataframe to check if it fits in power law
        '''

        df_log = np.log(df[['degree','counts']])
        models = ols('counts ~ degree', data = df_log).fit()
        print(models.summary())




