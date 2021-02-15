# Printing Bad Filenames
# surrogates mot allowed error

# when printing filenames of unknown origin,use the convention to avoid errors
import sys

# def bad_filename(filename):
#     return repr(filename)[1:-1]

# try:
#     print(filename)
# except UnicodeDecodeError:
#     print(bad_filename(filename))

import os
files = os.listdir('.')
# for name in files:
#     print(name)

# recipe for surrogates
# for name in files:
#     try:
#         print(name)
#     except UnicodeEncodeError:
#         print(bad_filename(name))

# re-encode the value in someway
def bad_filename(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')

for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))
