# dic datatype

std1 = {"Name": "Abdullah Maroof", "Roll No": "BAIM-S20-001", "Section": "2A"}
print(std1)
print("-------------------\n")

print("Accessing an item from dictionary\n")
access = std1["Roll No"]
print(access)
print("-------------------\n")

print("Accessing an item from dictionary by get()\n")
access = std1.get("Section")
print(access)
print("-------------------\n")

print("Changing value from dictionary\n")
std1["Roll No"] = "BSEM-S20-001"
print(std1)
print("-------------------\n")

print("Using for loop in dictionary to get key\n")
for key in std1:
    print(key)
print("-------------------\n")

print("Using for loop in dictionary to get values\n")
for value in std1:
    print(std1[value])
print("-------------------\n")

print("Use of values() in dictionary\n")
std1 = {"Name": "Shayan Gill", "Roll No": "BDSM-S20-020", "Section": "3A"}
for x in std1.values():
    print(x)
print("-------------------\n")

