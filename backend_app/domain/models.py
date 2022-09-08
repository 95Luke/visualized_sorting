from dataclasses import dataclass


@dataclass
class DataSet:
    db_name: str
    table_name: str
    records: list
