a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))

if a > b:
    print('{} is greater than {}'.format(a, b))
elif a < b:
    print('{} is smaller than {}'.format(a, b))
else:
    print('{} is equal to {}'.format(a, b))

