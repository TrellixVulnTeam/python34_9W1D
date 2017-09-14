def weekday(n):
    'returns the name of the nth day of the week'
    days = ['Monday', 'Tuesday', 'Wednesday']

    if 1 <= n and n <= 7:
        return days[n-1]
    
