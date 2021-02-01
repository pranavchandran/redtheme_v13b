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


