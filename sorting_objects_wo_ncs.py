# you want to sort objects of the same class,but they dont natively support comparison operations.
class User(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), (User(99))]
print(users)

# sorting
print(sorted(users, key=lambda w: w.user_id))

# Operator approach is more good compare to time 
# faster more items, also work in min and max
import operator
print(sorted(users, key=operator.attrgetter('user_id')))

