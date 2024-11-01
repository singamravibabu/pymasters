# imports
from datetime import date, time, datetime, timedelta

# days attribute to find numbers of days in timedelta object
span = timedelta(weeks=14, days=3, hours=100)
days_in_span = span.days
print("Days", days_in_span)

# seconds attribute - numbers of seconds in addtition to days
seconds_in_addition_to_days = span.seconds
print(seconds_in_addition_to_days)

# microseconds attribute - number of microseconds in addition to days and seconds
additional_microseconds = span.microseconds
print(additional_microseconds)

# totalseconds() method - retruns total seconds in a span of time
total_seconds = span.total_seconds()
print(total_seconds)