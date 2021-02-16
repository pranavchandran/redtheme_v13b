# serializing python objects
import pickle

data = object
f= open('somefile', 'wb')
pickle.dump(data, f)

# print(data.__dict__)

# dump an object to a string
# pickle.dumps()

s = pickle.dumps(data)
print(s)

# restore from a file
f = open('somefile', 'rb')
data = pickle.load(f)
# print(data)
# restore from a string
data = pickle.loads(s)

# pickle module

f = open('hello.txt', 'wb')
pickle.dump([1,2,3,4],f)
pickle.dump('hello',f)
pickle.dump({'apple','pear','banana'},f)
f.close()

# f = open('hello.txt', 'rb')
# print(pickle.load(f))
# print(pickle.load(f))
# print(pickle.load(f))

import countdown

c = countdown.Countdown(5)
print(c.run())
f = open('cstate.p', 'wb')
pickle.dumb(c, f)
f.close()

