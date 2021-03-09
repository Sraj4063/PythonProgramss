import time
currentTime = time.time()

# obtain the total seconds since midnight Jan 01 1970
totalSeconds = int(currentTime)

#Get the current second
currentSecond = totalSeconds % 60

# obtain the total minutes
totalMinutes = totalSeconds //60

# compute the current minute in the hour
currentMinute = totalMinutes % 60

# obtain the total hours
totalHours = totalMinutes // 60

# computer the current hour
currentHour = totalHours % 24

# Display resuls
print("current time is", currentHour, ":", currentMinute, ":", currentSecond, "GMT")