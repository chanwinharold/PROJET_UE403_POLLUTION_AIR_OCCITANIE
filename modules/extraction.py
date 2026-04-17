# CHANWIN Harold


import csv
import pandas as pd
import sqlite3 as sql

class DataManager:
    def __init__(self, filepath_: str=None):
        if filepath_:
            tmp = pd.read_csv(filepath_, dtype={'code_insee_com': str, 'dep_code': str})

            self.data_ = None
            self.filepath_ = filepath_
            self.types_ = {col_: type_ for col_, type_ in zip(tmp.columns.to_list(), tmp.dtypes.to_list())}
            self.data_length_ = tmp.shape[1]

    def read(self):
        with open(self.filepath_, mode='r') as file:
            reader_ = csv.DictReader(file)
            self.data_ = [tuple(row.values()) for row in reader_]

    @staticmethod
    def write(db_path_: str, filename_: str, query_: str):
        con, cur = sql.connect(db_path_), sql.connect(db_path_).cursor()
        res = cur.execute(query_).fetchall()
        with open(f"donnees/traitees/{filename_}", mode='w', newline= '') as file:
            writer = csv.writer(file)
            writer.writerow([col[0] for col in cur.description])
            writer.writerows(res)
        con.close()
