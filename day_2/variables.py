# Day 2: 30 Days of python programming
'''
first_name = 'Hadi '
last_name = 'Chowdhury'
full_name = first_name  + last_name
country = 'Bangladesh'
city = 'Dhaka'
age = 24
year = 2025
is_married = True
is_true = True
is_light_on = True

passport, nid = 'A0213124', '0981231511'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))

if len(first_name) < len(last_name):
    print(is_true)
else:
    print("false")
    

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one

exp = num_one ** num_two
print(remainder)

'''

# r = 30

# pi = 3.1416

# area_of_circle = pi * r **2

# print(area_of_circle)

# circum_of_circle = 2 * pi * r

# print(circum_of_circle)

radius = input('radius r = : ')
radius = int(radius)
pi = 3.1416
area_of_circle = pi * radius**2

print(round(area_of_circle, 2))