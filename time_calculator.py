#!/usr/bin/env python3

def add_time(start, duration, day_of_week=''):
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
    add = [int(i) for i in duration.split(':')]

    time[1] += add[1]

    if time[1] >= 60:
        time[1] -= 60

        if time[0] == 11 and period == pm:
            days += 1
            period = am

        time[0] += 1

    days += add[0] // 24
    add[0] -= (add[0] // 24) * 24
    remaining = 12 - time[0]

    if period == am:
        if add[0] < 12 and add[0] < remaining:
            time[0] += add[0]
        elif add[0] >= remaining and add[0] < (24 - time[0]):
            time[0] =  add[0] - remaining
            period = pm
        elif add[0] >= (24-time[0]):
            time[0] = add[0] - (remaining + 12)
            days += 1

    new_time = ''

    return new_time
