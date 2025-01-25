import duckdb
import argparse


class Count:

    def __init__(self, **kwargs):
        self.file = kwargs.get('file')
        self.distinct = kwargs.get('distinct')
        self.select = kwargs.get('select')
        self.group_by = kwargs.get('group_by')
        self.cursor = duckdb.connect().cursor()
        self.cursor.execute(
            f"""
                       SELECT COUNT({"DISTINCT " if self.distinct else ""} {self.select})
                       FROM "{self.file}"
                       {" GROUP BY " + " ".join(self.group_by) if len(self.group_by) > 0 else ""}
            """,
        )
        self.data = self.cursor.fetchall()

    def print(self):
        for entry in self.data:
            print(entry)


def count():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file',
        help='The filename of the parquet file to analyze'
    )
    parser.add_argument(
        '-d',
        '--distinct',
        default=False,
        action='store_true',
        help='Distinct count'
    )
    parser.add_argument(
        '-s',
        '--select',
        default='*',
        help='Column to select'
    )
    parser.add_argument(
        '-gb',
        '--group-by',
        nargs='*',
        default=[],
        help='Columns to group on'
    )
    Count(**vars(parser.parse_args())).print()
