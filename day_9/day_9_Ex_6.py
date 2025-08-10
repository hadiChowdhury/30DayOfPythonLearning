fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('Enter a fruit name: ')

if fruit in fruits:
    print('That fruit already exist in the list')
else:
    print('{} was not in the list. Adding in the list now'.format(fruit))
    fruits.append(fruit)
    print('Modified List: ', fruits)