def add_time(start, duration, weekday=None):

    #convering first letter to uppercase and rest of string to lowercase
    if weekday != None:
       weekday = weekday[0].upper() + weekday[1:].lower()

    time, period = start.split()
    hour, min = time.split(':')
    durhour, durmin = duration.split(':')

    daysofweek = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

    #convert to 24 hour format
    if int(hour) == 12 and period == 'AM':
        hour = '00'
    elif int(hour) == 12 and period == 'PM':
        hour = '12'
    elif int(hour) < 12 and period == 'AM':
        hour = hour
    else:
        hour = int(hour) + 12

    #converting to seconds
    startSeconds = int(hour) * 3600 + int(min) * 60
    durSeconds = int(durhour) * 3600 + int(durmin) * 60


    #adds start time to duration and converts it to days/hours/minutes
    days = int ((startSeconds + durSeconds) / 86400)
    hours = int (((startSeconds + durSeconds) % 86400 ) / 3600)
    minutes = ((((startSeconds + durSeconds) ) % 3600) / 60) / 100

    #variables that are used to display the new time after calculation
    newhour = hours
    newmin = minutes

    #converting back to 12 hour time
    if hours == 12:
        period = 'PM'
    elif hours == 0:
        newhour = 12
        period = 'AM'
    elif hours > 12:
        newhour = hours - 12
        period = 'PM'
    else:
        period = 'AM'

    #combining the new hour after converstion to the new minutes
    newtime = newhour + newmin
    newtime = '{:.2f}'.format(newtime) #formating decimal point
    newtime = newtime.replace('.', ':')

    if days == 1 and weekday == None :
        return (newtime + " " + period + " " + '(next day)')
    elif days == 1 and weekday != None:
        return (newtime + " " + period +"," + " " +  daysofweek[daysofweek.index(daysofweek[ (days % 7) - len(daysofweek[daysofweek.index(weekday):])])] ) + " "  + '(next day)'
    elif days > 1 and weekday == None:
        return (newtime + " " + period + " " + '('+ (str(days) + " " + 'days later' + ')' ))
    elif days == 0 and weekday != None:
        return (newtime + " " + period + "," + " " + weekday)
    elif days > 1 and weekday != None:
        return (newtime + " " + period +"," + " " +  daysofweek[daysofweek.index(daysofweek[ (days % 7) - len(daysofweek[daysofweek.index(weekday):])])]) + " " + '('+ (str(days) + " " + 'days later' + ')' )

    #returns the day in the week and time by taking the number that modular 7 of days returns minus the length of the weekday varible to the end of the daysofweek list.
    #ex) if days = 2 and weekday = Tuesday, the index of tuedsay in the list is 2 so we take the length of itself to the end of the list, which is 5. So we have part of the equation 'len(daysofweek.index(tuesday):] = 5. The modular of 2 % 7 = 2. So it looks like daysofweek[daysofweek.index(dayofweek [ 2 - 5] = -3
    #the day at the string slice -3 is Thursday.
    else:
        return (newtime + " " + period)


#-------------------------




#tests & notes
print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM
print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)
print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)
print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)

print(add_time("8:16 PM", "466:02"))
print(add_time("5:01 AM", "0:00"))
print(add_time("8:16 PM", "466:02", "Tuesday"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))

#convert time and duration into seconds
    #60 seconds in a minute
    #3600 seconds in an hour
    #86400 seconds in a day





##Assignment
#Write a function named add_time that takes in two required parameters and one optional parameter:

#a start time in the 12-hour clock format (ending in AM or PM)
#a duration time that indicates the number of hours and minutes
#(optional) a starting day of the week, case insensitive
#The function should add the duration time to the start time and return the result.

#If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

#If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

#Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

#dd_time("3:00 PM", "3:10")
# Returns: 6:10 PM

#add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

#add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

#add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

#add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

#add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)

#Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.