person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }  
}

if person.get('is_married') == True and person.get('country'):
    print('{} {} lives in {}. He is married.'.format(person.get('first_name'), person.get('last_name'), person.get('country')))