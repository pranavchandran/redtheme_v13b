# you want to redirect the output of the print() to a file
# use the file keyword argument to print(), like this
with open('hello.txt', 'wt')as f:
    print('hello pranav', file=f)

