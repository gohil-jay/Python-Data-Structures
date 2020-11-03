"""This is the date-time module."""

import datetime

def date_time():
    """This is a date function."""

    x = datetime.datetime.now() #complete date with time
    print(x) #complete date
    print(x.strftime("%c")) #Local date
    print(x.strftime("%x")) #Local Date
    print(x.strftime("%X")) #Local Time
    print("Year : ", x.year)
    print("Month : ", x.month)
    print("Day : ", x.day)
    print()
    print(x.strftime("%a")) #Day (short)
    print(x.strftime("%A")) #Day (Long)
    print(x.strftime("%b")) #Month (short)
    print(x.strftime("%B")) #Month (Long)
    print(x.strftime("%y")) #Year (short)
    print(x.strftime("%Y")) #Year (Long)
    print(x.strftime("%m")) #Month (Number)
    print(x.strftime("%M")) #Minute (Number)
    print(x.strftime("%d")) #Day (Number)
    print(x.strftime("%H")) #Hour (24hour)
    print(x.strftime("%I")) #Hour (12hour)
    print(x.strftime("%S")) #Second
    print(x.strftime("%f")) #MicroSecond
    print(x.strftime("%U")) #Week (Number)
    print(x.strftime("%j")) #Day (365)
    print(x.strftime("%w")) #Weekday
    print(x.strftime("%W")) #WeekNumber
    

    z = datetime.datetime(2012, 1, 1) #Create Date
    print()
    print("Created Date : ", z)

    date9 = datetime.datetime.strptime("2021-09-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
    print()
    print(date9)
    print()

date_time()
