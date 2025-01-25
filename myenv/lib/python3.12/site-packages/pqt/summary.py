import duckdb
import argparse


class Summary:

    def __init__(self, **kwargs):
        self.file = kwargs.get('file')
        self.lines = kwargs.get('lines')
        self.cursor = duckdb.connect().cursor()
        self.data = []

    def print(self):
        for entry in self.data:
            print(entry)


class Head(Summary):

    def __init__(self, **kwargs):
        Summary.__init__(self, **kwargs)
        self.cursor.execute(
            f"""
                SELECT * FROM "{self.file}" LIMIT ?
            """, [self.lines]
        )
        self.data = self.cursor.fetchall()


class Tail(Summary):

    def __init__(self, **kwargs):
        Summary.__init__(self, **kwargs)
        self.cursor.execute(
            f"""
                SELECT COUNT(*) FROM "{self.file}"
            """
        )
        count = self.cursor.fetchone()[0]
        skip = count - self.lines
        self.cursor.execute(
            f"""
                SELECT * FROM "{self.file}" LIMIT ? OFFSET ?
            """, [self.lines, skip]
        )
        self.data = self.cursor.fetchall()


def head():
    main('head')


def tail():
    main('tail')


def main(func):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file',
        help='The filename of the parquet file to analyze'
    )
    parser.add_argument(
        '-n',
        '--lines',
        default=10,
        type=int,
        help='Number of entries to show'
    )
    if func == 'head':
        Head(**vars(parser.parse_args())).print()
    elif func == 'tail':
        Tail(**vars(parser.parse_args())).print()
