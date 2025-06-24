import datetime
date = datetime.datetime.now()
print(date.strftime("The year is : %Y \n The date is : %D \n The month is : %B"))

transfer = datetime.date(2030,6,23)
print("\n",transfer)

# Enter a date
dates = datetime.date(2030,6,23)

# Enter a time
time = datetime.time(12,34,21)
print(time)
# Get todays date
print(date.strftime("The date is : %D")) 

# Time now
print(date.strftime("The time is : %X"))

