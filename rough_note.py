# # Question : Calculate the value of y. Where y = x^2 + 6x + 9. Try to use different x values and figure out at what x value  y is going to be 0.
# # Solutions:
#
# import random
#
# # Step 1: Function to calculate y
# def calculate_y(x):
#     return x*x + 6*x + 9
#
# # Step 2: Random search function
# def random_search_int(trials, low, high):
#     for i in range(trials):                     # repeat 'trials' times
#         x = random.randint(low, high)           # pick a random integer
#         y = calculate_y(x)                      # calculate y for that x
#         print("Trial", i+1, ": x =", x, "y =", y)
#
#         if y == 0:                              # check if we found a root
#             print("✅ Found a root! x =", x)
#             break                               # stop once we find it
#
# # Step 3: Call the function
# random_search_int(20, -20, 20)
#


# x= -3
# y = x*x + 6*x + 9
#
# print(y)

def calculate_y(x):
    return x**2 + 6*x + 9

range_start = -5
range_end = 5

zeros = []
non_zeros = []

for x in range(range_start, range_end +1):
    y = calculate_y(x)

    if y == 0:
        zeros.append(x)

    else:
        non_zeros.append(x)

print('when the value of x is {} y = 0'.format(zeros))
print('when the value of x is {} y!= 0'.format(non_zeros))
