#Tuple datatype

print("\n-----Tuple datatype-----\n")
std_name = ("Abdullah","Aneesa","Rehan","Shifa","Nisar","Sami","Waqas")
print(std_name)
print(type(std_name))
print("-----------------------------------------")

print("\nAccessing tuple item by postive index\n")
std_name = ("Abdullah","Aneesa","Rehan","Shifa","Nisar","Sami","Waqas")
print(std_name[3])
print("-----------------------------------------")

print("\nAccessing tuple item by negative index\n")
std_name = ("Abdullah","Aneesa","Rehan","Shifa","Nisar","Sami","Waqas")
print(std_name[-6])
print("-----------------------------------------")

print("\nAccessing tuple item by postive index range\n")
std_name = ("Abdullah","Aneesa","Rehan","Shifa","Nisar","Sami","Waqas")
print(std_name[1:5])
print("-----------------------------------------")

print("\nAccessing tuple item by negative index range\n")
std_name = ("Abdullah","Aneesa","Rehan","Shifa","Nisar","Sami","Waqas")
print(std_name[-5:-2])
print("-----------------------------------------")

print("\nAccessing tuple items by for loop\n")
std_name = ("Abdullah","Aneesa","Rehan","Shifa","Nisar","Sami","Waqas")
for name in std_name:
    print(name)
print("-----------------------------------------")

print("\nchecking an item in tuple by if & in\n")
std_name = ("Abdullah","Aneesa","Rehan","Shifa","Nisar","Sami","Waqas")
if "Nisar" in std_name:
    print("This name is the tuple: Nisar")
print("-----------------------------------------")

print("\nchecking an item in tuple by if & not in\n")
std_name = ("Abdullah","Aneesa","Rehan","Shifa","Nisar","Sami","Waqas")
if "Daniyal" not in std_name:
    print("This name is not the tuple: Daniyal")
print("-----------------------------------------")