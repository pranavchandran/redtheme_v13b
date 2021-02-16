# Read data from a csv file as tuples
import csv
# with open('stocks.csv') as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     for row in f_csv:
#         print(row)

# named tuple
from collections import namedtuple

# with open('stocks.csv') as f:
#     f_csv = csv.reader(f)
#     headings = next(f_csv)
#     print(headings)
#     Row = namedtuple('Row', headings)
#     for r in f_csv:
#         row = Row(*r)
#         print(row)

# read the data as a sequence of dictionaries
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        rows = row
        print(rows['Symbol'])



