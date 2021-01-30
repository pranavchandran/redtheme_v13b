# Data structure match the sequence

p = (4, 5)
x, y = p

print(x)
print(y)

data = ['asd', 50, 91.1, (2012, 12, 21)]
# name,shares,price,date = data
name,shares,price,(year, mon, day) = data

print(name)
print(shares)
print(price)
print(year)
print(mon, day)

s = 'Hello'
a, b, c, d, e = s 

print(a,d)

# throwway variable

_, _, c, _, _ = s 
print(c)

record = ('Pranav', 'pranav@gmail.com', '773-555-1212','9656888814')

name, email, *mobile = record

print(mobile)

*trailing, current = [10,1,2,3,6]
print(trailing)

# sequence of tagged tuples

records = [('foo', 1,2),('bar', 'hello'),('foo', 3, 4)]

def do_foo(x, y):
    print('foo', x,y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unpriveleged User:/var/empty:/usr/bin/false'

uname, *fields, homedir, sh = line.split(':')

print(uname)
print(homedir)
print(sh)

# making throw away variable
record = ('ACME', 50, 123.45, (12,18,2012))
name, *_,(*_,year) = record
print(name)
print(year)

items = [1,10,7,4,5,9]
head, *tail = items
print(head)

# writing a function 
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))
