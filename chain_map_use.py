# you have to check both dictionaries (first checking in A then B).An easy way to doing is 
# a chain map
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(type(c))
for x,y in c.items():
    print(x,y)
print(len(c))
print(list(c.keys()))
print(list(c.values()))

c['z'] = 10
c['w'] = 40
del c['x']

for x,y in c.items():
    print(x,y)

values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
values = values.parents
print(values['x'])
values = values.parents
print(values['x'])
print(values)

# for merging dictionaries we can use update() method
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])
a['x'] = 13
print(merged['x'])

# a chainmap uses the original dictionary so doesnt have this behaviour
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 42
print(merged['x'])





