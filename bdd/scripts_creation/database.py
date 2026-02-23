import sqlite3 as sql
from sqlite3 import Connection, Cursor
from script_Python.extraction import read_data


def open_connection(db_path_: str) -> tuple[Connection, Cursor]:
    connect_ = sql.connect(db_path_)
    cursor_ = connect_.cursor()
    return connect_, cursor_


def close_connection(connect_: Connection):
    connect_.close()

import pandas as pd
def get_creation_query(filepath_: str, table_name_: str):
    ith_row_ = read_data(filepath_=filepath_)[0]
    type_list_ = pd.read_csv(filepath_, nrows=1).dtypes.to_list()
    type_encoder_ = {
        'str': "TEXT",
        'object': "TEXT",
        'int64': "INT",
        'float64': "DECIMAL",
        'bool': 'BOOLEAN',
        'datetime64[ns]': 'DATETIME',
    }

    columns_ = ith_row_.keys()
    types_ = [type_encoder_[str(t)] for t in type_list_]

    attributes_ = ""
    for c, t in zip(columns_, types_):
        attributes_ += f"{c} {t}, "

    return f"CREATE TABLE IF NOT EXISTS {table_name_} ({attributes_[:-2]})"


def create_table(query_: str, cursor_: Cursor):
    cursor_.execute(query_)


def add_constraints(query_: str, cursor_: Cursor):
    cursor_.execute(query_)




connection, cursor = open_connection('../UE403_DB.db')

url = "../../donnees/brutes/donnees_socio_economiques.csv"
print(get_creation_query(filepath_=url, table_name_='UE403_Socio_economiques'))