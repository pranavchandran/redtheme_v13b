# Getting a directory listing

# Want to get a list of the files contained in a directory

# os.listdir()

import os

# names = os.listdir('/root/python_cook_book_david_beazley')

# for index,name in enumerate(names):
#     print('{}{:=>40s}'.format(index, name))

import os.path
# get all regular files
name = [name for name in os.listdir('/root/python_cook_book_david_beazley')
        if os.path.isfile(os.path.join('/root/python_cook_book_david_beazley/', name))]



# get all dirs
# dirnames = [name for name in os.listdir('/root/python_cook_book_david_beazley')
#             if os.path.isdir(os.path.join('/root/python_cook_book_david_beazley', name))]

# print('Directories =', [x for x in dirnames])

pyfiles = [name for name in os.listdir('/root/python_cook_book_david_beazley')
            if name.endswith('.py')]

# print(pyfiles)

# for filename matching use glob or fnmatch modules
import glob
binfiles = glob.glob('/root/python_cook_book_david_beazley/c5_files_and_io/*.bin')
# print(binfiles)
from fnmatch import fnmatch
binfiles = [name for name in os.listdir('/root/python_cook_book_david_beazley/c5_files_and_io/')
            if fnmatch(name, '*.bin')]

print(binfiles)

pyfiles = glob.glob('*.py')
# get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))for name in pyfiles]
# print(name_sz_date)
# for name, size, mtime in name_sz_date:
#     print('{},{:>35},{:>30}'.format(name, size, mtime))

# Alternative get file metadata
file_metadata = [(name, os.stat(name))for name in pyfiles]
print(file_metadata)

for name,meta in file_metadata:
    print('{:=>15}{:=>20}{:=>15}'.format(name, meta.st_size, meta.st_mtime))





