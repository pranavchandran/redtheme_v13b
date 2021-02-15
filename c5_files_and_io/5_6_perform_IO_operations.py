import io

s = io.StringIO()
print(s.write('Hello World\n'))
print(s.__sizeof__())
print('This  is  a  test',file=s)
# get all the data written so far
print(s.getvalue())

print(s.__sizeof__())

# wrap a file interface around an existing string

s = io.StringIO('Hello\nWorld\n')
print(s.read(4))

# operating with binarydata use the io.BytesIoclass
sb = io.BytesIO()
sb.write(b'binary data')
print(sb.getvalue())

