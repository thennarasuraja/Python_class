import datetime
'''
https://www.geeksforgeeks.org/python-datetime-module/

https://www.w3schools.com/python/python_datetime.asp

astimezone
combine
ctime
date
day
dst
fold
fromisocalendar
fromisoformat
fromordinal
fromtimestamp
hour
isocalendar
isoformat
isoweekday
max
microsecond
min
minute
month
now
replace ,resolution
second
strftime
strptime
time
timestamp
timetuple
timetz
today
toordinal
tzinfo
tzname
utcfromtimestamp
utcnow
utcoffset
utctimetuple
weekday
year
'''
# istTimeDelta = datetime.timedelta(hours=5.30)
# istTZObject = datetime.timezone(istTimeDelta,
#                                 name="IST")
# d1 = datetime.datetime.now()
# d2 = d1.astimezone(istTZObject)

# print("Indian time from a datetime instance:{}".format(d2))
#================================================================
#my_date = datetime.date(1996, 12, 11)
#================================================================
# my_date = datetime.date.today()
#================================================================
 
#print("Date passed as argument is", datetime.date.today().year, "month", datetime.date.today().month,"day", datetime.date.today().day)
#================================================================

# date_time = datetime.datetime.fromtimestamp(1668820478)
# print("Datetime from timestamp:", date_time)

# print(datetime.datetime.isoweekday(datetime.date(2022, 11, 20)))   #1-7 1- mon, 2-tue...7- sun
# print(datetime.date(2022, 11, 20).strftime("%w"))       #0-6    1 mon, 2-tue...0- sun

# print(datetime.date(2022, 11, 19).strftime("%a"))

# print(datetime.date(2022, 11, 19).strftime("%w"))

# print(datetime.date(2022, 11, 19).strftime("%d"))


# print(datetime.date(2022, 11, 19).strftime("%b"))

print(datetime.date(2022, 11, 19).strftime("%B"))

#d- day, m- month , y year.
# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	# %p	AM/PM	PM	

