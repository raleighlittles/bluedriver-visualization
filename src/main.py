import argparse
import os
import logging
import file_parser
import plotter

logging.basicConfig(level=logging.WARNING)

if __name__ == "__main__":
    files = os.listdir("data")

    logging.warning("Discovered {0} files in data folder".format( len(files)))

    dataframes = []
    for file in files:
        dataframes.append(file_parser.process_file(os.path.join("data", file)))

    logging.warning("{0} dataframes".format(len(dataframes)))
    plotter.create_aggregated_plot(dataframes)
