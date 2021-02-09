# if the strings you wish to combine are found in a sequence or iterable, the
# fastest way to combine them is to use the join() method.

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

a = 'Is Chicago'
b = 'Not Chicago'
print(a + ' ' + b)

print('{} {}'.format(a, b))
a = 'Hello'  'World'
print(a)

data = ['ACME', 50, 91.1]
print(','.join(str(d)for d in data))

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago'

text = ''.join(sample())
print(text)

# for part in sample():
#     f.write(part)

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)

        if size > maxsize:
            yield ' '.join(parts)
            parts = []
            size = 0
    yield ' '.join(parts)

import sys
# for part in sample():0
#     sys.stdout.write(part)
# sys.stdout.write('\n')

for part in combine(sample(), 32768):
    sys.stdout.write(part)
sys.stdout.write('\n')

# Interpolating variables in Strings
# Substituting variable values in strings

s = '{name} has {n} messages'
# print(s.format(name='Guido', n=37))

# using formatmap
name = 'Guido'
n = 37
print(s.format_map(vars()))

# Subtle feature of vars is that also work with instances
class info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

a = info('Guido', 37)

modified = s.format_map(vars(a))
print(modified)

del n
n = 'sasi'
print(s.format_map(safesub(vars())))

import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('hello {name}'))
print(sub('you have {n} messages'))
print(sub('{name} have {n} messages'))

# missing key
print('your favourite color is {color}')

# you will sometime see string formatting like this.
name = 'Guido'
n = 37
print('{%s} has {%s} messages'%(name,n))
# print('%(name) has %(n) messages.' %vars())

# template strings
import string

s= string.Template('$name has $n messages.')
print(s.substitute(vars()))







