# Removing Duplicates from a sequence while maintaining order
# hashable
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1,5,2,1,9,1,5,10]
print(list(dedupe(a)))

# if it is unhashable
def dedupe1(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a1 = [{'x': 1, 'y': 2}, {'x':1,'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe1(a1, key=lambda d: (d['x'],d['y']))))

a = [1,5,2,1,9,1,5,10]
print(set(a))

with open('somefile.txt','r')as f:
    for line in dedupe(f):
        print(line)
