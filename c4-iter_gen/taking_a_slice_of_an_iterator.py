# u want to take a slice of data produced by an iterator,but normal slicing operator doesn't work
# itertools.isslice() is the tool for iterators and generators

def count(n):
    while True:
        yield n
        n += 1

c = count(0)

import itertools
for x in itertools.islice(c, 10, 20):print(x)

# Skipping the first part of an iterable
# 1. itertools.dropwhile function
# reading a file with a lot of comment lines
# with open('/etc/passwd')as f:
#     for line in f:
#         print(line, end='')

# want to skip all the initial comment lines.
from itertools import dropwhile

with open('/etc/passwd')as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in itertools.islice(items, 3, None):
    print(x)

# 2 version 
with open('/etc/passwd')as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')








