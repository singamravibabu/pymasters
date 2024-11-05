# WORK WITH SPANS OF TIME
# Use the timedelta construct from datetime module
# to create a timedleta object use timedelta construct

# imports
from datetime import date, time, datetime, timedelta

# difference between two date/time objects to create timedelta
today = date.today()
bd_date = date(2024, 5, 15)
days_difference = today - bd_date  # timedelta object
print("Days passed since my birthday:", days_difference)
print(type(days_difference))
print()

# Syntax
# timedelta( [days][, seconds][, microseconds][, minutes][, hours][, weeks])
days_18 = timedelta(weeks=2, days=4)
print("Days:", days_18)

# the timedelta gives the outcome in days, seconds, and microseconds
project_duration = timedelta(hours=100, minutes=30)
print("Project Duration:", project_duration)

# trip duration: 3 weeks, 4 days, 8 hours, 34 minutes, 35 seconds
trip_duration = timedelta(weeks=3, days=4, hours=8, minutes=34, seconds=35)
print(trip_duration)

# if trip starts today the end date will be...
trip_ends_on = today + trip_duration
print("Trip Ends on...", trip_ends_on)