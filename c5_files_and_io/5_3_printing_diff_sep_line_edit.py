# Printing with a Different separator or Line Ending

# you want to output data using print(),but you also want to change the separator charcter
# or line ending.

# Use the sep and keyword arguments to print() to change the output as you wish

print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')

# suppress the output of newlines in output
for i in range(5):
    print(i)

for i in range(5):
    print(i, end=' ')

# sometimes you'll see programmers using str.join() to accomplish the samething
print(','.join(('ACME', '50', '91.5')))

row = ('ACME', 50, 91.5)
# print(','.join(row))
print(','.join((str(x) for x in row)))

# instead of doing that, you could just write the following
print(*row, sep=',')




