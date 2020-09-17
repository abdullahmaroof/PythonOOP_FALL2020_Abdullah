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






