# days to seconds, hours to minutes
# to repr an interval of time,create timedelta instance like this

from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b

print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds() / 3600)

from datetime import datetime

a = datetime(2012, 9, 23)
print(a + timedelta(days=10))

b = datetime(2012, 12, 2)
d = b - a
print('interval days',d.days)

now = datetime.today()
print('Time and Date: ',now)

print(now + timedelta(minutes=10))

# datetime is aware of leap years
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)

print(a - b)

c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print(c-d)

a1 = datetime(2012, 9, 23)
# print(a1 + timedelta(months=1)) month is an invalid keyword

from dateutil.relativedelta import relativedelta

print(a1 + relativedelta(months=+1))

print(a1 + relativedelta(months=+4))

# Time between 2 dates
b = datetime(2012, 12, 21)
d = b - a
print(d)
d = relativedelta(b, a)
print(d)
# print(d.months, d.days)

# Determining Last Friday's Date
# you want to find last occurence of a day of the week.Last friday Example.

from datetime import datetime,timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

print(get_previous_byday('Saturday'))

# performing same calculation using the relativedelta() function
# from dateutil

from dateutil.rrule import *
d = datetime.now()
# next friday
print(d + relativedelta(weekday=FR))
# last Friday
print(d + relativedelta(weekday=FR(-1)))











