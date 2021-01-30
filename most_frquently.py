# Determine the most frequently occuring items in the sequence

words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

morewords = ['why','are','you','not','looking','in','my','eyes']
more_counts = Counter(morewords)
for word in morewords:
    more_counts[word]+=1
print(more_counts['eyes'])

a = Counter(words)
b = Counter(morewords)
print(a)
print(b)

c = a+b
print(c)

d = a-b
print(d)



