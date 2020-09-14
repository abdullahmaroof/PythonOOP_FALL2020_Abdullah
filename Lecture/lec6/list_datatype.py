# List datatype
print("")
print("Printing a list")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
print(std)
print(type(std))
print("-----------------------------------------------\n")

print("Accessing an item in list")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
print(std[2])
print("-----------------------------------------------\n")

print("Accessing an item in list from right side")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
print(std[-1])
print("-----------------------------------------------\n")

print("Accessing items from list in a range")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
print(std[2:5])
print("-----------------------------------------------\n")

print("Accessing items from list in a range but only starting range")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
print(std[1:])
print("-----------------------------------------------\n")

print("Accessing items from list in a range but only ending range")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
print(std[:3])
print("-----------------------------------------------\n")

print("Accessing items from list in a negative range")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
print(std[-5:-2])
print("-----------------------------------------------\n")

print("Changing an item in list")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
std[2] = "Daniyal"
print(std)
print("-----------------------------------------------\n")

print("Printing list by for loop")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
for name in std:
    print(name)
print("-----------------------------------------------\n")

print("Checking an item in list by \"if\" and \"in\"")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
if "Shifa" in std:
    print("This name is in student list")
print("-----------------------------------------------\n")

print("Length of list")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
print(len(std))
print("-----------------------------------------------\n")

print("sorting list")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
std.sort()
print(std)
print("-----------------------------------------------\n")

print("Reverse list")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
std.reverse()
print(std)
print("-----------------------------------------------\n")

print("Checking index of item in list")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
print(std.index("Rehan")," ",std.index("Habiba"))
print("-----------------------------------------------\n")

print("Adding an item in list")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
std.append("Shahbaz")
print(std)
print("-----------------------------------------------\n")

print("Inserting an item in list by insert()")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
std.insert(2,"Ramzan")
print(std)
print("-----------------------------------------------\n")

print("Removing an item in list by remove()")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
std.remove("Waqas")
print(std)
print("-----------------------------------------------\n")

print("Removing last item in list")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
std.pop()
print(std)
print("-----------------------------------------------\n")

print("Removing an item in list from index by del")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
del std[2]
print(std)
print("-----------------------------------------------\n")

print("Emptying list by clear()")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
std.clear()
print(std)
print("-----------------------------------------------\n")

print("Copy of list by copy()")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
std1 = std.copy()
print(std1)
print("-----------------------------------------------\n")

print("Another way of copy of list by list()")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
std1 = list(std)
print(std1)
print("-----------------------------------------------\n")

print("Joining two list")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
std1 = ["Aneesa", "Akmal", "Rohan", "Naomi"]
std2 = std + std1
print(std2)
print("-----------------------------------------------\n")

print("Another way of joining two list")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
std1 = ["Aneesa", "Akmal", "Rohan", "Naomi"]
for std2 in std1:
    std.append(std2)
print(std)
print("-----------------------------------------------\n")

print("Another way of joining two list by extend()")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
std1 = ["Aneesa", "Akmal", "Rohan", "Naomi"]
std.extend(std1)
print(std)
print("-----------------------------------------------\n")

print("Another way of creating list by list(())")
std = list(("Aneesa", "Akmal", "Rohan", "Naomi","Abdullah", "Ali", "Rehan",))
print(std)
print("-----------------------------------------------\n")

print("Removing whole in list by del")
std = ["Abdullah", "Ali", "Rehan", "Shifa", "Waqas", "Habiba"]
del std
print(std)
print("-----------------------------------------------\n")


