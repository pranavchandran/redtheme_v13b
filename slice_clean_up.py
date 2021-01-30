'012345678901234567890123456789012345678901234567890123456789'
record = '.............................100             ,,,,,,,,,,,,,,,513.25 ........'
# cost = (int(record[20:32]))
# print(cost)

items = [0,1,2,3,4,5,6]
a = slice(2,4)
print(items[2:4])
print(items[a])

items[a] = [10,11]
print(items)

del items[a]
print(items)


a1 = slice(5, 50, 2)
print(a1.start)
print(a1.stop)
print(a1.step)

s = 'HelloWorldef'
a1.indices(len(s))
for i in range(*a1.indices(len(s))):
    print(s[i])

