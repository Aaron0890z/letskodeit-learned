import csv


def CSVReader(fileName):
    # create an empty list to store rows
    rows = []
    # open the csv file
    dataFile = open(fileName, "r")
    # create a CSV reader from CSV file
    reader = csv.reader(dataFile)
    # skip the readers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
