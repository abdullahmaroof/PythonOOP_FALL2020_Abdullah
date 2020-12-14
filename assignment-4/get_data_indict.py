file = open("studentData.txt", "r")
name = []
age = []
data = {}

for line in file:
    y = line.strip()
    if y.isdigit():
        age.append(y)
    else:
        name.append(y)

for i in name:
    data["name"] = i
    for x in age:
        data["age"] = x






# print(name)
# print(age)
file.close()
