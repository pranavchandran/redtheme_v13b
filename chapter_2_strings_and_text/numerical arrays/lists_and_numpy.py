# python lists
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x*2)
print(x+y)

# Numpy arrays
import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)

# value of a polynomial
def f(x):
    return 3*x**2 - 2*x+7

print(f(ax))

print(np.sqrt(ax))
print(np.cos(ax))

grid = np.zeros(shape=(1000, 1000),dtype=float)
print(grid)

# use all of the eleents simultaneously
grid += 10
print(grid)

print(np.sin(grid))

# 2 dimesional arrays and try some experiments
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[1])
# select column 1
print(a[:, 1])
# select a subregion and change it
print(a[1:3, 1:3])

a[1:3, 1:3] += 10
print(a)

# Broadcast a row vector across an operation on all rows
print(a + [100, 101, 102, 103])
print(a)

# conditional assignment on an array
print(np.where(a < 10, a, 10))











