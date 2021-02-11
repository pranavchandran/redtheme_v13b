# how you would represent a date in chicago time
from datetime import datetime
import pytz
from pytz import timezone, utc
from datetime import timedelta

# In 2013, US standard daylight saving time started on march 10,2.00 a.m

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

# Localize the data for chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print('Chicago TZ: ', loc_d)

# convert to Banglore time
bang_d = loc_d.astimezone(timezone('ASIA/Kolkata'))
print('Banglore time', bang_d)

d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
# print(loc_d)
# later = loc_d + timedelta(minutes=30)
# print(later)

# to fix this use the normalize() method of the timezone
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)

print(loc_d)

utc_d = loc_d.astimezone(utc)
print(utc_d)

later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))

print(pytz.country_timezones['IN'])
