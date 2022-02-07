import csv

def reader(filename):
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            yield line

def parse_transaction(lines):
    rows = csv.reader(lines)
    types = [int, str, int, str, int, str, float, str]
    converted = ([func(val) for func, val in zip(types, row)] for row in rows)
    return converted

def filter(rows, func):
    filtered = (row for row in rows if func(row))
    return filtered