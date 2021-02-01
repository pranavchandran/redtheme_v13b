import heapq

class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue,(-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q1 = PriorityQueue()
# print(q)
q.push(Item('foo'), 1)
q.push(Item('oof'), 2)
q.push(Item('bar'), 10)
q.push(Item('bar'), 4)
print(q.__dict__)

# q.push(Item('bar'), 5)
# q.push(Item('spam'), 4)
# q.push(Item('grok'), 1)

# print(q.__dict__)
# heapq.heapify(q.__dict__['_queue'])
# print('as',(q.__dict__))

# print(q.pop())
# print(q.__dict__)
# print(q.pop())
# print(q.__dict__)
# print(q.pop())
# print(q.pop())

a = (1, Item('foo'))
b = (5, Item('foo'))
print(a<b)

