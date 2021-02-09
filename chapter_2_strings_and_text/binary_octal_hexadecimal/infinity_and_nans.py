# floating point values of infinity,negative infinity or NaN
a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c)

# test for the presence of these values use the math.isinf() and math.isnan()
import math

print(math.isinf(a))
print(math.isnan(c))

a = float('inf')
print(a + 45)
print(a * 10)
print(10 / a)
print(a/a) #get not a num
b = float('-inf')
print(a + b)

# nan values propagate -> without raising exception
c = float('nan')
print(c + 23) #nan
c/2 #nan
c * 2 #nan
math.sqrt(c) #nan

# nan never compares as equal
c = float('nan')
d = float('nan')
c == d #false
c is d #false




