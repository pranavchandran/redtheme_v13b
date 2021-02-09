# Unicode letters

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1==s2)
print(len(s1), len(s2))

import unicodedata

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1==t2)
print(ascii(t1))
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3, t4, t3 == t4)

# NFKC and NFKD
s = '\ufb01'
print(s)

print(unicodedata.normalize('NFD', s))

print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))

t1 = unicodedata.normalize('NFD', s1)
res = ''.join(c for c in t1 if not unicodedata.combining(c))
print(res)

# working with unicode characters in regular Expressions
import re

num = re.compile('\d+')
# ASCII digits
print(num.match('123'))

print(num.match('\u0661\u0662\u0663'))

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
print(arabic)

pat = re.compile('stra\u00dfe', re.IGNORECASE)
print(pat)

s = 'straße'
print(pat.match(s))

print(pat.match(s.upper()))
print(s.upper())














