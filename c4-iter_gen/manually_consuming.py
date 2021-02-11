# you need to process items in an iterable,but for whatever reason,you can't or don't want 
# to use a for loop

# example1
# with open('/etc/passwd')as f:
#     try:
#         while True:
#             line = next(f)
#             print(line, end='')
#     except StopIteration:
#         pass

# example2
# with open('/etc/passwd') as f:
#     while True:
#         line = next(f, None)
#         if line is None:
#             break
#         print(line, end='')

# illustrates basic mechanics of what happens during iteration
items = [1, 2, 3]
# get the iterator
it = iter(items) #invokes iter function items.__iter__()
# Run the Iterator
print(next(it)) #invokes it.__next__()
print(next(it))
print(next(it))
print(next(it))


