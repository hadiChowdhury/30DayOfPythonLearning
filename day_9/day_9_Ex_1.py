#Conditionals_Statement
#1
age = input("Enter your age: ")
age = int(age)
print(age)

if age > 18 or age == 18:
    print("You are old enough to learn to drive.")
else:
    remain = 18 - age

    print("You need {} more years to learn to drive.".format(remain))

