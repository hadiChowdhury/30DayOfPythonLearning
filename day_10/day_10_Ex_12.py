fruit = ['banana', 'orange', 'mango', 'lemon']

reversed_list = []

for i in range(len(fruit) -1, -1, -1):
    reversed_list.append(fruit[i])

print(reversed_list)