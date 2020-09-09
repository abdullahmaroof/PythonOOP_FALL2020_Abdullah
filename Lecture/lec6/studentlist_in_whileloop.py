# student list by while loop


std_roll_no = []
std_name = []
std_father_name = []
std_section = []
std_dep = []
press = 1
condition = 0
print("Student record system")
print("-----------------------------------\n")
while condition < press:
    std_name.append(input("Enter name of new student: "))
    std_father_name.append(input("Enter father name of new student: "))
    std_roll_no.append(input("Enter roll no of new student: "))
    std_section.append(input("Enter section of new student: "))
    std_dep.append(input("Enter department of new student: "))
    print("---------------------------------------------------------\n")
    print("Do you want to enter a new record of student")
    enter = int(input("press 1 to enter or press 0 to save record: "))
    condition = condition + press
    press = press + enter
print("Your record is saved successfully!!!")
