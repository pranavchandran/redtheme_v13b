# you are trying to match a simple literal,you can often just use the basic string methods
# str.find(),str.endswith,str.startswith()
import re
text = 'yeah, but no, but yeah,but no, but yeah'

print(text=='yeah')

# match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
# simple matching \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')

# precompile the regular expression pattern into a pattern object first
datepat = re.compile(r'\d+/\d+/\d')
if datepat.match(text1):
    print('yes')
else:
    print('No')

if datepat.match(text2):
    print('yes')
else:
    print('No')

text = 'Today is 11/27/2012 PyCon starts 3/13/2013'
print(datepat.findall(text))

datepat1 = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat1.match('11/27/2012')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

month, day, year = m.groups()
print(text)
print(datepat1.findall(text))

for month, day, year in datepat1.findall(text):
    print('{}-{}-{}'.format(year, month, day))

for x in datepat1.finditer(text):
    print(x.groups())

m = datepat.match('11/27/2012abcdef')
print(m)
print(m.group())

# for exact match
datepat = re.compile(r'(\d+)/(\d+)/(\d)$')
x = datepat1.match('11/27/2012')
print(x.group())

# for simple literal patterns use the str.replace()
text1 = 'yeah, but no, but yeah, but no, but yeah'
print(text1.replace('yeah', 'yep'))

# rewriting the dates of the form
import re
filt_text = re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2', text)
print('example sub',filt_text)

# if you're going to perfrm repeated situations compiling it first for better performance

import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
filt_text_1 = datepat.sub(r'\3-\1-\2', text)
print(filt_text_1)

from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(datepat.sub(change_date, text))

newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)

















