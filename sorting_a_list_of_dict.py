# you have a list of dictionaries and you would like to sort the entries according
# to one or more of the dictionary values.
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
# from operator import itemgetter
# import pprint

# rows_by_fname = sorted(rows, key=itemgetter('fname'))
# # print('rows by fname',rows_by_fname)
# rows_by_uid = sorted(rows, key=itemgetter('uid'))
# # print('rows_by_uid',rows_by_uid)

# # itemgetter() can also accept multiple keys.
# rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
# print(rows_by_lfname)


class itemgetter_P:
    """
    Return a callable object that fetches the given item(s) from its operand.
    After f = itemgetter(2), the call f(r) returns r[2].
    After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
    """
    __slots__ = ('_items', '_call')

    def __init__(self, item, *items):
        if not items:
            self._items = (item,)
            def func(obj):
                return obj[item]
            self._call = func
        else:
            self._items = items = (item,) + items 
            def func(obj):
                return tuple(obj[i] for i in items)
            self._call = func

    def __call__(self, obj):
        return self._call(obj)

    # def __repr__(self):
    #     return '%s.%s(%s)' % (self.__class__.__module__,
    #                           self.__class__.__name__,
    #                           ', '.join(map(repr, self._items)))

    # def __reduce__(self):
    #     print('reduce',self.__class__, self._items)
    #     return self.__class__, self._items

# it = itemgetter_P(rows)
# print(it.__slots__)

# print(sorted(rows, key=itemgetter_P('fname','lname')))

# The functionality of itemgetter() is sometime replaced by lambda expressions
rows_by_fname_lm = sorted(rows, key=lambda k: k['uid']) 
print(rows_by_fname_lm)

# we can also use in min and max
print('Using minimum',min(rows, key=itemgetter_P('uid')))
