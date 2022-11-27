import pandas as pd
import matplotlib.pyplot as plt
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

    def plot_edges_distribution(self, occurence_list: list[int]):
        '''
        Plots the degree distribtuion of genes/nodes

        :param list[int] occurnce_list: each element in the list corresponds to the degree of a Gene in the GRN
        '''
        degree_dict = {}
        degree = 1
        for occurence in occurence_list:
            degree_dict[occurence] = degree_dict.get(occurence, 0) + 1
        print(degree_dict)
        print(degree_dict.keys())
        print(degree_dict.values())
        print(list)
        plt.scatter(degree_dict.keys(), degree_dict.values())
        plt.loglog()
        plt.show()
