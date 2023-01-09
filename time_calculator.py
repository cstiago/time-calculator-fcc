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
    later = ''
    new_time = ''
    
    period = start.split()[1]
    time = [int(i) for i in start.split()[0].split(':')]
    add = [int(i) for i in duration.split(':')]

    time[1] += add[1]

    if time[1] >= 60:
        time[1] -= 60

        if time[0] == 11:
            if period == am:
                period = pm
            elif period == pm:
                period = am
                days += 1

        time[0] += 1

    days += add[0] // 24
    add[0] -= (add[0] // 24) * 24

    if time[0] == 12:
        remaining = 12
    else:
        remaining = 12 - time[0]

    if add[0] < 12 and add[0] < remaining:
        time[0] += add[0]
    else:
        if period == am:
            if add[0] >= remaining and add[0] < (remaining + 12):
                time[0] = add[0] - remaining
                period = pm
            elif add[0] >= (24-time[0]):
                time[0] = add[0] - (remaining + 12)
                days += 1
        elif period == pm:
            days += 1
            if add[0] >= remaining and add[0] < (remaining + 12):
                time[0] = add[0] - remaining
                period = am
            elif add[0] >= (24-time[0]):
                time[0] = add[0] - (remaining + 12)

    if time[0] > 12:
        time[0] -= 12

    time = ':'.join(str(i) for i in time)
    new_time += ' '.join([time, period])

    if day:
        new_time += ' '.join([',', day])

    if days == 1:
        later = '(next day)'
    elif days > 1:
        later = f'({days} days later)'

    if later:
        new_time = ' '.join([new_time, later])

    return new_time
