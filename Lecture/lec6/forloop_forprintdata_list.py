# student list by while loop and user will tell condition and printing by for loop

std_roll_no = []
std_name = []
std_father_name = []
std_section = []
std_dep = []
print("Student record system")
print("-----------------------------------\n")
condition = int(input("Tell how many student data you want to enter: "))
print("-----------------------------------\n")
std_index = 0
while (std_index < condition):
    std_name.append(input("Enter name of new student: "))
    std_father_name.append(input("Enter father name of new student: "))
    std_roll_no.append(input("Enter roll no of new student: "))
    std_section.append(input("Enter section of new student: "))
    std_dep.append(input("Enter department of new student: "))
    print("---------------------------------------------------------\n")
    std_index = std_index + 1

print("Your record is saved successfully!!!")
print("---------------------------------------------------------\n")
for studentdata in range(0,condition):
    print("Name of student: ", std_name[studentdata])
    print("Father name of student: ", std_father_name[studentdata])
    print("Roll no of student: ", std_roll_no[studentdata])
    print("Section of a student: ", std_section[studentdata])
    print("Department of a student", std_dep[studentdata])
    print("------------------------------------------------\n")
