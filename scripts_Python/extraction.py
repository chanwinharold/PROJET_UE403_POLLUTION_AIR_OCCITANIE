import csv
import pandas as pd


class DataManager:
    def __init__(self, filepath_: str):
        tmp = pd.read_csv(filepath_, dtype={'code_insee_com': str, 'dep_code': str})

        self.data_ = None
        self.filepath_ = filepath_
        self.types_ = {col_: type_ for col_, type_ in zip(tmp.columns.to_list(), tmp.dtypes.to_list())}
        self.data_length_ = tmp.shape[1]

    def read(self):
        with open(self.filepath_, mode='r') as file:
            reader_ = csv.DictReader(file)
            self.data_ = [tuple(row.values()) for row in reader_]
