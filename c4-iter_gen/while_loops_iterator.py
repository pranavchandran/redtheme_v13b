# Replacing infinite while loops with an iterator
# somewhat common scenario in programs involving I/O is to write code like this.

CHUNKSIZE = 8192
def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break;
        process_data(data)

# using iter()
def reader(s):
    for chunk in iter(lambda s: s.recv(CHUNKSIZE), b''):
        process_data(chunk)

# you're skeptical that it might work, you can try a similar example involving files
import sys
# f = open('/etc/passwd')
# for chunk in iter(lambda:f.read(10), ''):
#     n = sys.stdout.write(chunk)

'''
fo = open("foo.txt", "rw+")
print "Name of the file: ", fo.name

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fo.read(10)
print "Read Line: %s" % (line)

# Close opend file
fo.close()
'''
fo = open("foo.txt", "r")
print("Name of the file: ", fo.name)
for chunk in iter(lambda : fo.read(10), ):
    n = sys.stdout.write(chunk)

