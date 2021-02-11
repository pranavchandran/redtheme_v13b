"""Want to implement a new kind of iteration pattern,define it using a generator function.
Generator that produces a range of floating-point numbers"""

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))

# experiment can try to see the underlyig mechanics of how sucha func works
def countdown(n):
    print('Starting to count from ',n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

# create the gen no output appeas
c = countdown(3)
print(c)
try:
    while c:
        print(next(c))
except StopIteration as x:
    print('sorry try')




