import csv
import pandas as pd 

def read_csv_header(path):
    pass


def read_csv_data(path):
    with open(path, "r") as file:
        df = pd.read_csv(file, usecols=[0,1,2,3,4,5,6], delimiter=",")
        list_of_rows = [list(row) for row in df.values]
    return list_of_rows

