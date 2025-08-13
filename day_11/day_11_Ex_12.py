food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]

def remove_item(lst, item):
    lst.remove(item)
    return lst
print(remove_item(food_staff, 'Mango'))
print(remove_item(numbers, 3))