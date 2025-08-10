number = int(input('Enter your number: '))

if number > 80 and number <= 100:
    print('Grade A')
elif number >= 70 and number <= 89:
    print('Grade B')
elif number >= 60 and number <= 69:
    print('Grade C')
elif number >= 50 and number <= 59:
    print('Grade D')
else:
    print('Grage F')