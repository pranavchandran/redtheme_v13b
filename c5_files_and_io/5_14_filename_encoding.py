# Bypassing Filename Encoding
import sys

sys.getfilesystemencoding()

# write a file using a unicode filename
with open('jalape\xf10.txt', 'w') as f:
    f.write('Spicy!')

# Directory listing (decoded)
import os

# print(os.listdir('.'))

# Directory listing raw
# print(os.listdir(b'.')) #Note: byte string

# open file with raw filename
# with open(b'jalape\xf10.txt') as f:
#     print(f.read())

