def sum_of_odds(n):
    total = 0
    for i in range(n+1):
        if i % 2 != 0:
            total = total + i
    return total
print(sum_of_odds(7))