# Reading and writing textdata
# u can do it in (ASCII, UTF-8, UTF-16)

# Read the entire file as a single string
with open('somefile.txt', 'rt') as f:
    data = f.read()
# print(data)

# Iterate over the lines of the file
with open('somefile.txt', 'rt') as f:
    for line in f:
        print(line)

# clearing and overwriting the previous contents.
# with open('somefile.txt', 'a') as f:
#     f.write('\nPranav is a Pythonista')

# with open('somefile.txt', 'rt') as f:
#     data = f.read()
# print(data)

# Redirected print statement
# with open('somefile.txt', 'wt') as f:
#     print(line1, file=f)

# if not using with remeber to close the file
# f = open('somefile.txt', 'rt')
# data = f.read()
# f.close()

# g = open('hello.txt', 'rt', newline='')
# print(g.read())

# f = open('hello.txt', 'rt', encoding='ascii')
# print(f.read())

# Replace bad chars with Unicode U+fffd replacement char
f = open('hello.txt', 'rt', encoding='ascii', errors='replace')
print(f.read())

f = open('hello.txt', 'rt', encoding='ascii', errors='ignore')
print(f.read())





