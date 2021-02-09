# Fractions
from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
print(a*b)

# getting numertor and denominator
c = a * b
print(c.numerator)
print(c.denominator)

# converting to a float
print(float(c))

# Limiting the denominator of a value
print(c.limit_denominator(8))

# converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())

print(y)
