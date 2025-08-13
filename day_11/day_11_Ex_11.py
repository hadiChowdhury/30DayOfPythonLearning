food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3 , 7, 9]
def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item(food_staff, 'Meat'))
print(add_item(numbers, 10))