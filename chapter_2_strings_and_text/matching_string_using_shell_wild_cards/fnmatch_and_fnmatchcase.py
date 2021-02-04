from fnmatch import fnmatch,fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
filtered = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(filtered)

addresses = [
    '5412 N CLARK ST',
    '5148 N CLARK ST', 
    '5800 E 58TH',
    '2122 N CLARK ST',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

addr_filt = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(addr_filt)

addr_filt2 = [addr for addr in addresses if fnmatchcase(addr, '5[0-9][0-9]*CLARK*')]
print(addr_filt2)

