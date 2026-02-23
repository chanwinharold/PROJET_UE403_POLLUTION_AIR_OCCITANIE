import csv
from typing import Any


def read_data(filepath_: str) -> list[dict[str | Any, str | Any]]:
    with open(filepath_, mode='r') as file:
        reader_ = csv.DictReader(file)
        return [row for row in reader_]