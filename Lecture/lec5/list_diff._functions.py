# use of list
bsse_2A = [400, 300, 430, 670, 300]
bsse_1A = bsse_2A


print(bsse_2A)
print(bsse_1A)
print("------------------------------------")

bsse_2A = [300, 400, 90, 40]
print(bsse_2A)
print("-------------------------------------")

bsse_2A = [40, 200, 460, 900, 200]
bsse_1A = bsse_2A

bsse_2A.append(200)
print(bsse_1A)
print(bsse_2A)
print("---------------------------------------")

bsse_2A = [40, 200, 460, 900, 200]
bsse_1A = bsse_2A.copy()
bsse_2A.append(350)
print(bsse_1A)
print(bsse_2A)
print("---------------------------------------")

bsse_2A = [40, 200, 460, 900, 200]
bsse_1A = bsse_2A.copy()
bsse_1A.insert(3,30)
print(bsse_1A)
print(bsse_2A)
print("---------------------------------------")

bsse_2A = [40, 200, 460, 900, 870]
bsse_1A = bsse_2A.copy()
bsse_1A.insert(3,30)
bsse_2A.sort()
bsse_1A.sort()
print(bsse_1A)
print(bsse_2A)
print("---------------------------------------\n\n")

list1 = [1, 3, 5, 67, 12]
list2 = [1, 5, 6, 21, 45, 32]
print(len(list1))
print("---------------------------------------")
print(len(list2))
print("---------------------------------------")
print(len(bsse_1A))
print("---------------------------------------")
print(len(bsse_2A))
print("---------------------------------------")
