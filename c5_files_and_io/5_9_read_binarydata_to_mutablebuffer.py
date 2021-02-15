# Reading binary data into a mutable buffer
import os.path

def read_info_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

# illustrates the usage
with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_info_buffer('sample.bin')
print(buf)

buf[0:5] = b'Hare'
print(buf)

with open('newsample.bin', 'wb') as f:
    f.write(buf)

# Equally sized records
record_size = 32
buf = bytearray(record_size)
with open('somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break

print(buf)

m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)

m2[:] = b'WORLD'
print(buf)
