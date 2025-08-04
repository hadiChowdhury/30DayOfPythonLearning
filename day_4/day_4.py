'''
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)
print('I hope everyone is enjoying the Challenge. \nAre You ?')
print('Days\tTopics\tExercises')
print('Days\t5\t5')
print('This is a backslash symbol (\\)')
first_name = 'Shihab'
last_name = 'Chowdhury'
language = 'python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)
first_name = 'Shihab'
last_name = 'Chowdhury'
language = 'Python'

formated_string = 'I am {} {}. I am learning {}'.format(first_name, last_name, language)

print(formated_string)


# company = 'Coding For All'
# print(company.swapcase())

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.3f}.'.format(radius, area) # 3 digits after decimal
print(formated_string)

'''
# name = 'shihab'

# first_letter = name[0]

# print(first_letter)

# last_index = len(name) - 1
# print(last_index)
# last_letter = name[last_index]
# print(last_letter)

var = "Coding For All"

print(var[0:6])

search = "Coding"

print(var.replace('Coding', 'Python'))

print(var.split(' '))

toSplit = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(toSplit.split(','))

print(var[0])
last_index = len(var) -1
print(last_index)

print(var[10])

a = 8 
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} + {} = {}".format(a, b, a - b))
print("{} + {} = {}".format(a, b, a * b))
print("{} + {} = {}".format(a, b, a / b))
print("{} + {} = {}".format(a, b, a % b))
print("{} + {} = {}".format(a, b, a // b))
print("{} + {} = {}".format(a, b, a ** b))

radius = 10
area = 3.14 * radius ** 2

print('The area of a circle with radius {} is {:.2f} meters square.'.format(radius, area))
