#1
dog = {}
print(type(dog))

#2
dog['name'] = 'ZOY'
dog['color'] = 'Black'
dog['breed'] = 'German'
dog['legs'] = 4
dog['age'] = 12

print(dog)

#3
student = {
    'first_name' : 'Shihab',
    'last_name' : 'Chowdhury',
    'gender' : 'male',
    'age' : 24,
    'marital_status': 'single',
    'skills':['Linux', 'React', 'Node', 'Python'],
    'country' : 'Bangladesh',
    'city' : 'Dhaka',
    'address': { 
        'street':'Space street',
        'zipcode':'02210'
    }
}
#4
print(len(student))

#5
skills = student.get('skills')
print(skills)
print(type(skills))

#6
student['skills'].append('HTML')
print(skills)

#7
print(student.keys())

#8
print(student.values())

#9
print(student.items())

#10
del student['address']
print(student)

#11
del student