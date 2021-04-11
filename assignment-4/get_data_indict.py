file = open("studentData.txt", "r")
name = []
age = []
data = {'name': name, 'age': age}

for line in file:
    y = line.strip()
    if y.isdigit():
        age.append(y)
    else:
        name.append(y)








print(data)
file.close()
