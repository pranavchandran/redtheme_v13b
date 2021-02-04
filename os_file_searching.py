import os
files = os.listdir('./')
import heapq
# print(files)
if any(name.endswith('.py')for name in files):
    print('There be python')
else:
    ('Sorry, no python.')

# output a tuple as csv
s = ('ACME', 50, 123.45)
gen_s = (','.join(str(x)) for x in s)
print(list(gen_s))

# data reduction across fields of a data structure.
portfolio = [
   {'name':'GOOG', 'shares': 50},
   {'name':'YHOO', 'shares': 75},
   {'name':'AOL', 'shares': 20},
   {'name':'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['shares'])
print(cheap)

nums = [1,2,3,4,5]
# more elegant syntax
s2 = sum(x*x for x in nums)
print(s2)

min_shares_1 = min(portfolio, key=lambda s: s['shares'])
print(min_shares_1)
