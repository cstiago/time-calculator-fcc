#!/usr/bin/env python3

def add_time(start, duration, day=''):
    am, pm= 'AM', 'PM'
    days_of_week = (
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    )
    days = 0
    
    period = start.split()[1]
    time = [int(i) for i in start.split()[0].split(':')]
    duration = [int(i) for i in duration.split(':')]

    time[1] += duration[1]

    if time[1] >= 60:
        time[1] -= 60

        if time[0] == 11 and period == pm:
            days += 1
            period = am

        time[0] += 1

    new_time = ''

    return new_time
