from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# create a prototype instance
stock_prototype = Stock(' ', 0, 0.0, None, None)

def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name':'aCME', 'shares':100, 'price':123.45}
b = {'name':'aCME', 'shares':100, 'price':123.45, 'date': '12/17/2020'}

print(dict_to_stock(a))
print(dict_to_stock(b))

# calculate the sm of squares
nums = [1,2,3,4,5]
s = sum(x for x in nums)
print(s)


