# Adding or Changing the encoding of an already Open File

import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()
# print(text)

import sys
# print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin1')
# print(sys.stdout.encoding) #latin1

# trying the simple example involving a text file
f = open('sample.txt', 'w')
# print(f)
# print(f.buffer)
# print(f.buffer.raw)

f = io.TextIOWrapper(f.buffer, encoding='latin-1')
# print(f)

# f.write('namaskar') #io operation in closed file

g = open('sample.txt', 'w')
print(g)
b = g.detach()
print(b)
# g.write('hello') #underlying buffer has been detached
g = io.TextIOWrapper(b, encoding='latin-1')
print(g)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii', errors='xmlcharrefreplace')
print('Jalape\u00f1o')



