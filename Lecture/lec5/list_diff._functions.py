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