import argparse
import os
import sys
import pandas
import typing.List

import src.plotter

def generate_bluedriver_plots_from_data(input_directory : str, output_directory : str):

    input_files: typing.List[str] = os.listdir(input_directory)

    if input_files is None:
        print(f"No files found in directory: {input_directory}")
        return 1

    print(f"{len(input_files)} files found.")

    dataframes = []
    
    for file in input_files:
        # First 2 rows in Bluedriver data files are the heading and the date.
        dataframes.append(pandas.read_csv(os.path.join(args.i, file), skiprows=2))

    src.plotter.create_aggregated_plot(dataframes, args.o)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-folder", help="Input directory: where Bluedriver data files are stored", type=str, required=True)
    parser.add_argument("-o","--output-folder", help="Output directory: where output graphs will be stored", type=str, required=True)
    args = parser.parse_args()

    generate_bluedriver_plots_from_data(args.input_folder, args.output_folder)

    



