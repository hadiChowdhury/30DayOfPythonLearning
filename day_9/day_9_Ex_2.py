my_age = input('Enter my age: ')
my_age = int(my_age)
your_age = input('Enter your age: ')
your_age = int(your_age)

if my_age > your_age:
    dif = my_age - your_age

    if dif > 1:
        print("I am {} years older than you".format(dif))
    else:
        print("I am {} year older than you".format(dif))

elif your_age > my_age:
    dif = your_age - my_age

    if dif > 1:
        print("You are {} years older than me".format(dif))
    else:
        print("You are {} year older than me".format(dif))

else:
    print("You and me both are same age")
