def minutes_to_hours(seconds, minutes=70):
    hours = minutes / 60 + seconds / 3600
    print(hours)

def seconds_to_hours(seconds):
    hours  = seconds / 3600
    return hours

print(type(minutes_to_hours(300, 200)))

