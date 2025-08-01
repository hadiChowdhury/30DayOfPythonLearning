# Day 1 - 30DaysOfPython Challenge
import math
print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

## Find an Euclidian distance between (2, 3) and (10, 8) ##

x1 = 2
y1 = 3

x2 = 10
y2 = 8

a = x2 - x1
b = y2 - y1

distance = math.sqrt((a)**2 + (b)**2)

print(distance)