# use of class in python

print("")
print("-----------------Use of class------------")
print("")
class std:
    name = ""
    rollno = ""
    section = ""

std1 = std()
std1.name = "Abdullah Maroof"
std1.rollno = "BAIM-S20-001"
std1.section = "2A"

std2 = std()
std2.name = "Muhammad Hafeez"
std2.rollno = "BAIM-S20-002"
std2.section = "2A"

std3 = std()
std3.name = "Aneesa Ashraf"
std3.rollno = "BAIM-S20-003"
std3.section = "2A"

print("\n----------------Student data------------")
print("\n   Name          |     Roll no    | Section")
print(std1.name," | ",std1.rollno," |   ",std1.section)
print(std2.name," | ",std2.rollno," |   ",std2.section)
print(" ",std3.name," | ",std3.rollno," |   ",std3.section)