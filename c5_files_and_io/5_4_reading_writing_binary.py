# Reading and writing binary data
# you need to write binary data such as that found in images,sound files etc

# open() 'rb' or 'wb' read or write binary data.
# with open('somefile.bin', 'wb')as f:
#     data = f.write(b'Hello World')

# with open('somefile.bin', 'rb')as f:
#     data = f.read()
#     print(data)

# Byte string
# b = b'Hello world'
# print(b[0])

# for c in b:
#     print(c)

# read or write text from a binary-mode file-> encode or decode it
# with open('somefile.bin', 'rb')as f:
#     data = f.read(10)
#     text = data.decode('utf-8')
#     print(text)

# with open('somefile.bin', 'wb')as f:
#     text = 'Hello Pranav'
#     f.write(text.encode('utf-8'))

# with open('somefile.bin', 'rb')as f:
#     data = f.read()
#     text = data.decode('utf-8')
#     print(text)

import array

nums = array.array('i', [1,2,3,4])
with open('data.bin', 'wb')as f:
    f.write(nums)

a = array.array('i', [0,0,0,0,0,0,0,0,])
with open('data.bin', 'rb')as f:
    print(f.readinto(a))

print(a)



