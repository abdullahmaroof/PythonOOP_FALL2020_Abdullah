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

for i in range(0,len(name)):
        data["name"+str(i)]= name[i]
        data["age"+str(i)] = age[i]






print(data)
file.close()
