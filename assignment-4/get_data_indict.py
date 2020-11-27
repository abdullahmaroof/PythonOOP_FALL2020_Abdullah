file = open("studentData.txt","r")
name = []

for line in file:
    name.append(line.strip())
print(name)
file.close()


