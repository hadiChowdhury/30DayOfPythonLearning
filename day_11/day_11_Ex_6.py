def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        print('Value is undefined')
    else:
        rise = y2-y1
        run = x2 - x1
        value = rise/run
        return(value)
print(calculate_slope(1, 1, 2, 4))