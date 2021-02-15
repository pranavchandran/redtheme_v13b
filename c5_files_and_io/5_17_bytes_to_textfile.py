# Writing Bytes to a text file
import sys
# sys.stdout.write(b'Hello\n')
print(sys.stdout.buffer.write(b'Hello\n'))
