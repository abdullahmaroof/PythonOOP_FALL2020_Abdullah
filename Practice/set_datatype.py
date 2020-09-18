# set datatype

set1 = {"Apple","Banna","Orange","Lemon"}
print(set1)
print(type(set1))
print("------------------------------")
print("Set is same like tuple but it doesn't have key for every item")
print("It has no fix order everytime you run programmer it order will be change")
print("-------------------------------------------------\n")

#Accessing items by for loop
stdname = {"abdullah","Sami","Aneesa","Shifa","Akmal"}
for name in stdname:
    print("Student name: ",name)
print("-----------------------------------------\n")

#checking an item in set
print("We cannot check index of a item because everytime it is changing order,so we can check this item is in set or not")
stdname = {"abdullah","Sami","Aneesa","Shifa","Akmal"}
print("Akmal" in stdname)
print("-----------------------------------------------\n")

#Adding item in set
print("If i want to add one item in set i will use add()")
print("But if i want to add more than one item i will use update()")
stdname = {"abdullah","Sami","Aneesa","Shifa","Akmal"}
stdname.add("Farah")
print(stdname)
print("-----------------------------")
stdname.update(["Kamran","Dania","Hafsa"])
print(stdname)
print("------------------------------------------------")
print("\n--------------------------------------------------\n")

#checking length of set
stdname = {"abdullah","Sami","Aneesa","Shifa","Akmal"}
print("The lenth of stdname set is:",len(stdname))
print("---------------------------------------------\n")

#Removing all the items from set by clear()
stdname = {"abdullah","Sami","Aneesa","Shifa","Akmal"}
stdname.clear()
print(stdname)
print("---------------------------------------------\n")

#difference between two sets
stdname1 = {"abdullah","Sami","Aneesa","Shifa","Akmal"}
stdname2 = {"abdullah","Shayan","Raftaar","Shifa","Akmal","Tooba"}
stdname = stdname1.difference(stdname2)
print(stdname)
stdname = stdname2.difference(stdname1)
print(stdname)
print("---------------------------------------------\n")



#Removing an item from set by discard()
stdname = {"abdullah","Sami","Aneesa","Shifa","Akmal"}
stdname.discard("Shifa")
print(stdname)

