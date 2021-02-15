# Iterating in sorted order over merged sorted iterables
# heapq.merge()

import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)

# with open('sorted_file_1', 'rt')as file1,open('sorted_file_2','rt') as file2,\
#     open ('merged_file', 'wt')as outf:
#     for line in heapq.merge(file1, file2):
#         outg.write(line)

list1 = [1,2,3,4,5]
def li(x):
    yield from x

print(next(li(list1)))
for x in li(list1):
    print(x)