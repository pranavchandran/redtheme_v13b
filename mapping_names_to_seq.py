from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(issubclass(Subscriber, tuple))
print(sub.addr)
print(sub.joined)

addr, joined = sub
print(addr)
print(joined)

# some code using ordinary tuples
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
records = [
    ('GOOG', 100, 490.1),
    ('ACME', 100, 123.45),
    ('IBM', 50, 91.15)
]

def compute_cost(records):
    total = 0.0
    for key in records:
        s = Stock(*key)
        print(s)
        total += s.shares * s.price
    return total

print(compute_cost(records))

# named tuple values can be replace only by _replace()
s1 = Stock('ACME', 100, 123.45)
print(s1)
# s1.shares = 200 #can't set attribute
s1 = s1._replace(shares=240)
print(s1)

