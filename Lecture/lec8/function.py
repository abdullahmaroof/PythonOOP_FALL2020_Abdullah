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
#def std_name():
 #   name = []
  #  for index in range(0, 2):
   #     name.append(input("Enter name of new student: "))
    #print(name)

#std_name()

#Getting data by user in function by while loop
def student():
    name = []
    index = 0
    while (index < 2):
        name.append(input("Enter name of new student: "))
        index = index + 1
    print(name)

student()





