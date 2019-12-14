import pandas
import matplotlib

def process_file(csv_filename : str, row_to_start_on = 2) -> pandas.core.frame.DataFrame:
    """
    Takes a CSV file and turns it into a pandas dataframe.
    :param csv_filename: The path to a CSV file.
    :return: 
    """
    with open(csv_filename, 'r') as csv_file:
        heading = [next(csv_file) for line in range(0, row_to_start_on)]

    title_line, date_line = heading

    return pandas.read_csv(csv_filename, skiprows=row_to_start_on)