# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(output_path, data, header):
    """Writes to a CSV file from path provided.

    Args:
        output_path (Path): The csv file path.
        data : data rows written to csv file
        header : column headers for csv file

    Returns:
        A list of lists with the rows of data to a CSV file.

    """


            # Open the output CSV file path using 'with open'
    with open(output_path, "w", newline="") as csvfile:
    
            # Create a csvwriter to hold the writer object
        csvwriter = csv.writer(csvfile)
            # Write the header to the CSV file
        csvwriter.writerow(header)
            # Write the values of qualifying loans list as a row in the CSV file    
        for row in data:
            csvwriter.writerow(row)
        return data    