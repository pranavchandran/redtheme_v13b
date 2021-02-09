# text operations on byte strings

data = b'Hello World'
print(data[0:5])

print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello',b'Cruel'))

data = b'FOO:BAR,SPAM'
import re

print(re.split(b'[:,]', data))

# indexing of byte string produces integers
b = b'Hello World'
print(b[0], b[1])

# decoding to ascii
s = b'Hello World'
print(s.decode('ascii'))

# print(b'{} {} {}'.format(b'ACME', 100, 490.1))
print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))

with open('jalape\xf1o.txt', 'w')as f:
    f.write('spicy')

# get a directory listing
import os
os.listdir('.')  #txt string names are decoded
['jalapeño.txt']

os.listdir(b'.')
print([b'jalapen\xcc\x830.txt'])