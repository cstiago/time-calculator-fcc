#!/usr/bin/env python3

def add_time(start, duration, day=''):
    tomorrow = '(next day)'
    n = 0
    later = '(' + str(n) + ' days later'

    days = (
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    )

    time = start.split()[0].split(':')
    period = start.split()[1]
    duration = duration.split(':')
    
    new_time = ''
    
    return new_time
