# nlargest and nsmallest
import heapq

nums = [1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print('Cheap :',cheap)
print('Expensive :', expensive)

# Example 3
nums_1 = [1,8,2,23,7,-4,18,23,42,37,2]
heap = list(nums_1)
heapq.heapify(heap)
print(heap)

print(heapq.heappop(heap))
print(heap)

heapq.heappush(heap,100)
print(heap)

ko = []
heapq.heapify(ko)
print(type(ko))