import sqlite3 as sql
from sqlite3 import Connection, Cursor
from scripts_Python.extraction import DataManager


class DBCreation:
    def __init__(self, db_path_: str):
        self.connect_: Connection | None = None
        self.cursor_: Cursor | None = None
        self.db_path_: str = db_path_

    def open_connection(self):
        self.connect_ = sql.connect(self.db_path_)
        self.cursor_ = self.connect_.cursor()

    def close_connection(self):
        self.connect_.close()

    def create_table(self, filepath_: str, table_name_: str):
        self.open_connection()
        manager_ = DataManager(filepath_=filepath_)
        manager_.read()

        type_list_ = manager_.types_.values()
        type_encoder_ = {
            'str': "TEXT",
            'object': "TEXT",
            'int64': "INTEGER",
            'float64': "REAL",
            'bool': 'BOOLEAN',
            'datetime64[ns]': 'DATETIME',
        }

        columns_ = manager_.types_.keys()
        types_ = [type_encoder_[str(t)] for t in type_list_]

        attributes_ = ""
        for c, t in zip(columns_, types_):
            attributes_ += f"{c} {t}, "

        self.cursor_.execute(f"CREATE TABLE IF NOT EXISTS {table_name_} ({attributes_[:-2]})")
        self.close_connection()

    def add_primary_key(self, table_name_: str, attribute_name_: str):
        self.open_connection()
        self.cursor_.execute(f"ALTER TABLE {table_name_} (ADD PRIMARY KEY ({attribute_name_}))")
        self.close_connection()

    def add_foreign_key(
        self,
        table_primary_: str,
        table_foreign_: str,
        attribute_primary_: str,
        attribute_foreign_: str
    ):
        self.open_connection()
        self.cursor_.execute(f"ALTER TABLE {table_primary_} (ADD FOREIGN KEY ({attribute_primary_}) REFERENCES {table_foreign_} ({attribute_foreign_}))")
        self.close_connection()

    def drop_table(self, table_name_: str):
        self.open_connection()
        self.cursor_.execute(f"DROP TABLE IF EXISTS {table_name_};")
        self.close_connection()

    def insert_values(self, filepath_: str, table_name_: str):
        self.open_connection()
        manager_ = DataManager(filepath_=filepath_)
        manager_.read()

        unknowns = '?, ' * manager_.data_length_
        self.cursor_.executemany(f"INSERT INTO {table_name_} VALUES ({unknowns[:-2]})", manager_.data_)
        self.connect_.commit()
        self.close_connection()

    def execute_query(self, query_: str):
        self.open_connection()
        self.cursor_.execute(query_)
        self.close_connection()