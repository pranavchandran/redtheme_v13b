# list comprehension is good for filter data
mylist = [1,4,-5,10,-7,2,3,-1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

# generator expressions to produce the filtered values iteratively
pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
    print(x)

# filtering criteria
values = ['1','2','-3','-','4','N/A','5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int,values))
print(ivals)

# power to transform the data at the sametime
import math
print([math.sqrt(n) for n in mylist if n>0])

clip_neg = [n if n>0 else 0 for n in mylist]
print(clip_neg)

clip_pos = [n if n<0 else 0 for n in mylist]
print(clip_pos)
