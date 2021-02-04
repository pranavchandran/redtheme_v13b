# check the start or end of a string for specific text patters

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file'))
url = 'http://www.python.org'
print(url.startswith('http:'))

import os

filenames = os.listdir('.')
# print(filenames,'\n')
filtered1 = [name for name in filenames if name.endswith('.txt')]
print(filtered1)

print(any(name.endswith('.py')for name in filenames))

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

# choices = ['http:', 'ftp:']
# url = 'http://www.python.org'
# url.startswith(choices)

print(read_data('http://www.python.org'))

filename = 'spam.txt'
filename[-4:] == '.txt'
url = 'http://www.python.org'
url[:5] == 'http:' or url[:6] = 'https' or url[:4] == 'ftp:'

import re
re.match('http:|https:|ftp:', url)





