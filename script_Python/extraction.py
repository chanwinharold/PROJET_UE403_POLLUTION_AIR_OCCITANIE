import csv
from typing import Any


def read_data(filename_: str) -> list[dict[str | Any, str | Any]]:
    with open(filename_, mode='r') as file:
        reader_ = csv.DictReader(file)
        return [row for row in reader_]


data = read_data('../donnees/brutes/donnees_geo_climatiques.csv')
