# function

#Simple function
def stdname():
    print("Student names")
    print("* Abdullah")
    print("* Shifa")
    print("* Rehan")
    print("* Akmal")

stdname()

#getting data in function by for loop
def std_name():
    name = []
    for index in range(0, 2):
        name.append(input("Enter name of new student: "))
    print(name)

std_name()

#Getting data by user in function by while loop
def student():
    name = []
    index = 0
    while (index < 2):
        name.append(input("Enter name of new student: "))
        index = index + 1
    print(name)

student()

#getting data in function by for loop and user will also tell how many students age
def std_age():
    age = []
    endrange = int(input("How many students age you want to enter: "))
    for index in range(0, endrange):
        age.append(input("Enter age of new student: "))
    print(age)

std_age()

#getting data in function by while loop and user will also tell how many students age

def stdage():
    age = []
    endrange = int(input("How many students age you want to enter: "))
    while 0 < endrange:
        age.append(input("Enter age of new student: "))
        endrange = endrange - 1
    print(age)

stdage()

#conditions in function
def man_age():
    print("Welcome to your system")
    age = int(input("Enter your age: "))
    if age > 18:
        print("\nYou can go ahead because you are 18+")
    else:
        print("\nYou are not 18+, you cannot go into your system")
    print("Thank you to coming in our system")

man_age()
