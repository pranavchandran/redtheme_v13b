# rounding numerical values
# simple rounding
print(round(1.23, 1))
print(round(1.27, 1))
print(round(1.25362, 3))

a = 1627731
print(round(a, -1))
print(round(a, -2))
print(round(a, -3))

x = 1.23456
print(format(x, '0.2f'))
print(format(x, '0.3f'))
print('value is {:0.3f}'.format(x))

a = 2.1
b = 4.2
c = a + b
# c = round(c, 2)
# print(c)

# float they cant accurately represent base-10 decimals
print(a + b == 6.3)

# you want more performance you can use the decimal module
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)

print((a + b) == Decimal(6.3))

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)

nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums)) #1 disappears

import math
print(math.fsum(nums))

x = 1234.56789
# 2 decimal places of accuracy
print(format(x, '0.2f'))

# right justified in 10 chars, one digit accuracy
print(format(x, '>10.1f'))

# left justified
print(format(x, '<10.1f'))

# centred
print(format(x, '^10.1f'))

print(format(x, ','))

print(format(x, '0,.1f'))

print(format(x, 'e'))

print(format(x, '0.2E'))

x = 1234.56789
print(format(x, '0,.1f'))
print(format(-x, '0,.1f'))

swap_separators = {ord('.'): ',', ord(','):'.'}
print(format(x, ',').translate(swap_separators))

print('%0.2f'%x)
print('%10.1f'%x)
print('%-10.1f'%x)



















