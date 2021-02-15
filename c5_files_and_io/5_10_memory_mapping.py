# memory mapping 
# Binary Files

import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

# Access_READ for the access argument
# m = memory_map(filename, mmap.ACCESS_READ)
# modify the data locally,dnt want changes written back to original file
# use mmap.ACCESS_COPY
# m = memory_map(filename, mmap.ACCESS_COPY)

m = memory_map('data')
print(len(m))
print(m[:10])
print(m[0])

# Reassign a slice
m[0:13] = b'Amme Narayana'
print(m[:13])
# m.close()
# Memoryview of unsigned integers
v = memoryview(m).cast('I')
v[0] = 7
print('Where is it', m[0:4])
m[0:4] = b'\x07\x01\x00\x00'
print(v[0])


# Verify that changes that made
with open('data', 'rb') as f:
    print(f.read(13))

with memory_map('data') as m:
    print(len(m))
    print(m[0:10])
    # print(m.closed)

# # Memoryview of unsigned integers
# v = memoryview(m).cast('I')
# v[0] = 7
# print(m[0:4])
