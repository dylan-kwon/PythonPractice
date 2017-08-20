# coding=utf-8
from __future__ import print_function
from datetime import datetime, timedelta

now = datetime.now()
print(now)

print('\n')

str_date = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
print('%s, type = %s' % (str_date, type(str_date)))

date1 = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
print('%s, type = %s' % (date1, type(date1)))

print('\n')

date2 = date1.replace(year=2016, month=12, day=10, hour=10, minute=25, second=3)
print(date2)

print('\n')

# d = datetime.date(2015, 4, 15)
# t = datetime.time(12, 23, 38)
# dt = datetime.combine(d, t)
# print dt

print('\n')

nowTuple = now.timetuple()
print(nowTuple)
print(type(nowTuple.tm_year))
print(nowTuple.tm_mon)
print(nowTuple.tm_mday)
print(nowTuple.tm_hour)
print(nowTuple.tm_min)
print(nowTuple.tm_sec)

print('\n')

nowDelta = now + timedelta(days=1, weeks=5)
print(nowDelta)

print('\n')

