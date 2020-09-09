# student list by while loop


std_roll_no = []
std_name = []
std_father_name = []
std_section = []
std_dep = []
condition = True
print("Student record system")
print("-----------------------------------\n")
while condition == True:
    std_name.append(input("Enter name of new student: "))
    std_father_name.append(input("Enter father name of new student: "))
    std_roll_no.append(input("Enter roll no of new student: "))
    std_section.append(input("Enter section of new student: "))
    std_dep.append(input("Enter department of new student: "))
    condition = False
    print("---------------------------------------------------------\n")
    print("Do you want to enter a new record of student")
    press = input("Press 1 to enter or press 0 to save record: ")
    if press == 1:
        condition == True
    else:
        condition == False
print("\nRecord is saved successfully!!!")