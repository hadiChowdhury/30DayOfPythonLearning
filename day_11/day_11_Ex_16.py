def evens_and_odds(n):
    total_odd = []
    total_even = []

    for i in range(n+1):
        if i % 2 == 0:
            total_even.append(i)
        if i % 2 != 0:
            total_odd.append(i)

    return len(total_odd), len(total_even)
even, odds = evens_and_odds(100)
print("The number of evens are", even)
print("The number of odds are", odds)