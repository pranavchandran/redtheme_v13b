# Reading and writing compressed data files
# gzip compression

import gzip

# with gzip.open('somefile.gzip', 'rt') as f:
#     text = f.read()

# print(text)

# bz2 compression
import bz2

# with bz2.open('somefile.bz2', 'rt') as f:
#     text = f.read()

text = 'Some one not agreed.'
# write compresses data
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

# setting compresslevel Default level is 9
with gzip.open('somefile1.gz', 'wt', compresslevel=5) as f:
    f.write(text)

f = open('somefile1.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()

print(text)



