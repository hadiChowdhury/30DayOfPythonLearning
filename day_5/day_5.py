lst = []

print(len(lst))

lst = ['item1', 'item2', 'item3', 'item4', 'item5']

print('task2: ', lst)
print(len(lst))

print(lst[0])
print(lst[2])
print(lst[-1])

mixed_data_types = ['Shihab', '24', '172.45', 'Single', 'Dhaka']

#8
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))

#9
print(it_companies[0] + ' ' + it_companies[2] + ' ' + it_companies[-1])

#10
it_companies[0] = 'ZeuZ'

print(it_companies)
#11
it_companies.append('Meta')
print(it_companies)

#12
it_companies.insert(3, 'BestBrain')
print(it_companies)

#13
it_companies[0] = it_companies[0].upper()
print(it_companies)

#14
joined_string = '#; '.join(it_companies)
print(joined_string)

#15
print('ZEUZ' in it_companies)

#16
print(it_companies)
print(sorted(it_companies))  

#17
reversed_list = sorted(it_companies, reverse=True)
print(reversed_list)

#18
first_3_company = it_companies[0:3]
print(first_3_company)
#19
last_3_company = it_companies[-3:]
print(last_3_company)

#20
print(it_companies)
middle_it_company = it_companies[4]
print(middle_it_company)

#21
it_companies.remove('Meta')
print(it_companies)

#22
del it_companies[4]
print(it_companies)

#23
len_company = len(it_companies) -1
del it_companies[len_company]
print(it_companies)

#24
len_company = len(it_companies) +1
del it_companies[0:len_company]

print(it_companies)
#25
del it_companies
# print(it_companies)

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined_list = front_end + back_end

print(joined_list)

#27
full_stack = joined_list.copy()

#################### Exercises Level 2 ##############################3
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

ages.insert(0, 19)
print(ages)

ages.insert(11, 26)
print(ages)

middle = ages[len(ages) // 2]
print("Middle age: ", middle)

medianAge = middle / 2
print('Median age: ', medianAge)

total = sum(ages)
number = len(ages)
print(number)
average_age = total / number
print(average_age)

min_age = min(ages)
print(min_age)
max_age = max(ages)
print(max_age)

range_of_list = max_age - min_age
print(range_of_list)

com_valu_one = abs(min_age - average_age)
print(com_valu_one)
com_valu_two = abs(max_age - average_age)
print(com_valu_two)

