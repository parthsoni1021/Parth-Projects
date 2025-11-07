import datetime as dt

now = dt.datetime.now()
print(now, type(now))

year = now.year
month = now.month   # day, hour, minute, weekday(0 for monday) etc all are there
if year == 2025 and month > 10:
    print('2026 about to come')
    
    
date_of_birth = dt.datetime(year=2004,month=7,day=21)  #hour, min, second are default set as 0
print(date_of_birth)