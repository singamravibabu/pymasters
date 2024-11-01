from datetime import date, time, datetime

# date constructor today() function
aaj = date.today()
print("Today function:", aaj)

# datetime constructor now() function
ab = datetime.now()
print("Now function:", ab)

# date constructor
# date(year, month, day)
birthday = date(2024, 10, 15)
print("Birthday:", birthday)

# datetime(year, month, day[, hour][, minute][, day][, microsecond])
seminar_day_time = datetime(2024, 11, 5, 10, 30, 0)
print("Seminar Day and Time:", seminar_day_time)

# time(hour, minute, second, microsecond)
meeting_time = time(14, 30, 0)
print("Meeting time:", meeting_time)


# string date
dt1 = "2024/10/30"
dt2 = "4-25-2023"
dt3 = "15 8 2022"
dt4 = "On 5th Month, day 7, year 2020, at 10 and 30 minuts we met."

# use strptime() method to parse date and time from a string
date1 = datetime.strptime(dt1, "%Y/%m/%d")
print("Date 1:", date1)
date2 = datetime.strptime(dt2, "%m-%d-%Y")
print("Date 2:", date2)
date3 = datetime.strptime(dt3, "%d %m %Y")
print("Date 3", date3)
date4 = datetime.strptime(dt4, "On %mth Month, day %d, year %Y, at %H and %M minuts we met.")
print("Date4:", date4)
print("\n")
# use strftime() to format a datetime value
seminar = seminar_day_time.strftime("Day: %B %d, %Y (%A)\nTime: %I:%M %p")
print(seminar)
