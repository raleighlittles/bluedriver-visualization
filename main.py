import argparse
import os
import sys
import pandas
import src.plotter
from typing import List

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("i", help="Input directory: where Bluedriver data files are stored.", type=str)
    parser.add_argument("o", help="Output directory: where output graphs will be stored.", type=str)
    args = parser.parse_args()

    input_files: List[str] = os.listdir(args.i)

    if input_files is None:
        print("No files found in directory: {0}".format(args.i))
        sys.exit(1)

    print("{0} files found.".format(len(input_files)))

    dataframes = []
    for file in input_files:
        # First 2 rows in Bluedriver data files are the heading and the date.
        dataframes.append(pandas.read_csv(os.path.join(args.i, file), skiprows=2))

    src.plotter.create_aggregated_plot(dataframes, args.o)



