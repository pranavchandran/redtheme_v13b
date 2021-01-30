# using ordered dict
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

print(d)
for key in d:
    print(key, d[key])
import sys
print(sys.getsizeof(d))


import json
print(json.dumps(d))

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(),prices.keys()))
print('Minimum price is ',min_price)

max_price = max(zip(prices.values(),prices.keys()))
print('Maximum price is ',max_price)

# to rank the data
print(sorted(zip(prices.values(), prices.keys())))

print(min(prices))
print(max(prices))

print(min(prices.values()))
print(max(prices.values()))

lmin = min(prices, key=lambda k: prices[k])
print(lmin)
lmax = max(prices, key=lambda k: prices[k])
print(lmax)

min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)

# If there is duplicated values
prices = {'AAA': 45.25, 'ZZZ': 45.25}
print(min(zip(prices.values(),prices.keys())))
print(max(zip(prices.values(),prices.keys())))






