# Iterating over fixed size records
from functools import partial

RECORD_SIZE = 40

with open('somefile.txt', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)


