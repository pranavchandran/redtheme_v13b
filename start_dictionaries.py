from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

e = {}
e.setdefault('a', []).append(1)
e.setdefault('a', []).append(2)
e.setdefault('b', []).append(4)

print(e)

pairs = e
f = {}
for key, value in pairs.items():
    if key not in f:
        f[key] = []
    f[key].append(value)
print(f)

# defaultdict simply leads ot much cleaner code
d = defaultdict(list)
for key, value in pairs.items():
    d[key].append(value)
print('default_dict :', d)


