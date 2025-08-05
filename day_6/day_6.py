empty_tuple = ()

sister = ('Mishu', 'Disha')
brother = ('Shakil', 'Shohid')

siblings = sister + brother
print(siblings)

print(len(siblings))

parents = ('Awal', 'Shirin')

family_members = siblings + parents

print(family_members)

parents = family_members[-2:]
print(parents)
siblings = family_members[0:4]
print(siblings)

# Fruits tuple
fruits = ('Apple', 'Banana', 'Mango', 'Orange')

# Vegetables tuple
vegetables = ('Carrot', 'Spinach', 'Potato', 'Broccoli')

# Animal products tuple
animal_products = ('Milk', 'Eggs', 'Cheese', 'Chicken')

food_stuff_tp = fruits + vegetables + animal_products

print(food_stuff_tp)

food_stuff_lst = list(food_stuff_tp)
print(food_stuff_lst)

middle_item_tuple = food_stuff_tp[len(food_stuff_tp)//2]
print(middle_item_tuple)

middle_item_list = food_stuff_lst[len(food_stuff_lst)//2]
print(middle_item_list)

first_three_item = food_stuff_lst[0:3]
print(first_three_item)
last_three_item = food_stuff_lst[-3:]
print(last_three_item)

# del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
