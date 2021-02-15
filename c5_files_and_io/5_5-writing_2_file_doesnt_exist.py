# you want to write data to a file,but only if it doesnt already exist

with open('somenew', 'wt') as f:
    f.write('Hello\n')

# with open('somenew', 'xt') as f:
#     f.write('Hello\n')


# with open('somenew1', 'xt') as f:
#     f.write('Hello\n')

# file in binary mode, use mode xb 
# Alternative solution is to first test for the file like this

import os

if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists')

