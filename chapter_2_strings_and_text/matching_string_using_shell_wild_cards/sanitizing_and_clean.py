s = 'python\fis\tawesome\r\n'
remap = {ord('\t'): ' ', ord('\f'): ' ', ord('\r'): None}
a = s.replace('python', 'pranav')
print(s)
# a = s.translate(my_map)
print('mapping',a)

import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
# unicodedata.combining(chr(c))

b = unicodedata.normalize('NFD', s)
print(b)

print(b.translate(cmb_chrs))

# Maps all unicode decimal digit characters to their equivalent in ASCII
digitmap = {c:ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if unicodedata.category(chr(c))=='ND'}
print(len(digitmap))

# Arabic digits
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

print(s)

b = unicodedata.normalize('NFD', s)
b.encode('ascii', 'ignore').decode('ascii')
print(b)

print(b.translate(remap))

# white space removal function
def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s


