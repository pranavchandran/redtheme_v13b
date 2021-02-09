# Performing complex
a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)

print(a.real)
print(a.imag)
print(a.conjugate())

# In addition all of the usual mathematicla operators work
print(a + b)

print(a * b)

print(a / b)

print(abs(a))

# additional complex-valued functions(sines, cosines, squarerotts)
import cmath
print('cmath', cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

import numpy as np 

a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a + 2)
print(np.sin(a))

# make complex maths use cmath
print(cmath.sqrt(-1))
















