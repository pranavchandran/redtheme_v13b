import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
finded = str_pat.findall(text1)
print(finded)

str_pat_v0 = re.compile(r'\"(.*?)\"')
text2 = 'Computer says "no."Phone says "yes".'
finding = str_pat_v0.findall(text2)
print(finding)



