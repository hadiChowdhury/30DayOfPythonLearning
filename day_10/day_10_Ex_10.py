total_evens = 0
total_odds = 0

for i in range(101):
    if i % 2 == 0:
        total_evens = total_evens + i
    
    if i % 2 != 0:
        total_odds = total_odds + i

print("The sum of all evens is {}. And the sum of all odds is {}.".format(total_evens, total_odds))