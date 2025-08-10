person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }  
}

print(person.get('skills'))


if 'skills' in person:
    print('Skill is in the person dict')

    if 'Python' in person.get('skills'):
        print('Python is in the list')
        print(person.get('skills'))
    else:
        print('python is not in the skill list')
    
else:
    print('None')