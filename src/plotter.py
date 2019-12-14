import matplotlib.pyplot as plt
import re
import os

def create_aggregated_plot(dataframes, output_dir : str):
    """
    Create scatter plots for every possible column.

    :param frames: List of pandas dataframes.
    :param output_dir: The directory where the final plots will be stored.
    :return: None
    """

    largest_column_list = max([df.columns.tolist() for df in dataframes], key=len)

    # The first column in the Bluedriver data format is Time.
    for column in largest_column_list[1:]:
        for df in dataframes:
            if column in df.columns:
                plt.scatter(df['Time (s)'], df[column], s=1)

        plt.title(column)
        plt.xlabel("Time (s)")
        output_filename = os.path.join(output_dir, re.sub(r'\W', "", column) + ".svg")
        plt.savefig(output_filename)
        plt.clf()
