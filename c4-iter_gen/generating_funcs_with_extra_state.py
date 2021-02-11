# you would like to define a generator func,but it involves extra state that you would
# like to expose to the user somehow.
from collections import deque

class linehistory:
    def __init__(self, lines, histlen=10):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

with open('myfile1.txt')as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, oline in lines.history:
                print('{}:{}'.format(lineno, oline), end='')

