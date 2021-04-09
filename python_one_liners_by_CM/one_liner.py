'''
Let’s consider the same employee salary problem introduced
earlier: given a dictionary with string keys and integer values,
create a new list of (key, value) tuples so that the value
associated with the key is larger than or equal to 100,000.
'''
# Data
employees = {'Alice' : 100000,
'Bob' : 99817,
'Carol' : 122908,
'Frank' : 88123,
'Eve' : 93121}

top_earners = [(k,v) for k,v in employees.items() if v > 100000]
print(top_earners)

# 2nd
'''
The Basics
Search engines rank textual information according to its
relevance to a user query. To accomplish this, search engines
analyze the content of the text to be searched. All text consists
of words. Some words provide a lot of information about the
content of the text—and others don’t. Examples for the former
are words like white, whale, Captain, Ahab (Do you know the
text?). Examples for the latter are words like is, to, as, the, a,
or how, because most texts contain those words. Filtering out
words that don’t contribute a lot of meaning is common
practice when implementing search engines. A simple
heuristic is to filter out all words with three characters or less.
'''

## Data
text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

w = [[x for x in line.split() if len(x)>3]for line in text.split('\n')]
# result
# print(w)
# for line in text.split('\n'):
#     for x in line.split():
#         if len(x)> 3:
#             print(x)
