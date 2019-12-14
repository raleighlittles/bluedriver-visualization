import matplotlib.pyplot as plt
import logging
import pdb
import re

def create_aggregated_plot(dataframes):
    """
    Create plots of each columns in the dataframe against time.
    :param frames: List of dataframes
    :return:
    """

    largest_column_list = max([df.columns.tolist() for df in dataframes], key=len)

    print("Longest columns are: {0}".format(len(largest_column_list)))

    for column in largest_column_list[1:]:
        # Go thru each dataframe and create a graph of Time vs the given column. Save the plot at the end.
        for df in dataframes:
            if column in df.columns and column != "Time (s)":
                plt.scatter(df['Time (s)'], df[column], s=1)

        plt.title(column)
        plt.xlabel("Time (s)")
        plt.savefig(re.sub(r'\W', "", column) + ".svg")
        plt.clf()
