import random

values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))

print(random.sample(values, 2))

print(random.sample(values, 3))

# shuffle items
print(random.shuffle(values))
print(values)

# produce random integers,use random.randint()
print(random.randint(0,10))

# to produce uniform floating-point values in the range 0 to 1
# use random.random()

print(random.random())

# to get N random-bits expressed as an integer,use random.getrandbits():
random.getrandbits(200)

# random.seed()
# a seed based on system time or os.urandom()
random.seed(12345)
random.seed(b'bytedata')





