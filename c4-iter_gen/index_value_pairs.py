# Iterating over the index value pairs of a sequence

# built in enumerate() handles this

# my_list = ['a', 'b', 'c']
# for idx, val in enumerate(my_list):
#     print(idx, val)

# start numbering at 1 instead of 0
# for idx, val in enumerate(my_list, 1):
#     print(idx, val)

# should you want to use a line number in an error message
# def parse_data(filename):
#     with open(filename, 'rt')as f:
#         for lineno, line in enumerate(f, 1):
#             fields = line.split()
#             try:
#                 count = int(fields[1])
#             except ValueError as e:
#                 print('Line {}: Parse error: {}'.format(lineno, e))
# myfile = './myfile1.txt'
# parse_data(myfile)
# def parse_data(filename):
#     with open(filename, 'rt') as f:
#          for lineno, line in enumerate(f, 1):
#              fields = line.split()
#              print(**fields)
#              try:
#                  count = yield from fields
#                  print(list(count))
#              except ValueError as e:
#                  print('Line {}: Parse error: {}'.format(lineno, e))

# print(parse_data('sample.dat'))
from collections import defaultdict

word_summary = defaultdict(list)
with open('myfile1.txt', 'r')as f:
    lines = f.readlines()
    # print(lines)

for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)

data = [(1,2), (3,4), (5,6), (7,8)]

for n,(x,y) in enumerate(data):
    print(n,(x,y))



