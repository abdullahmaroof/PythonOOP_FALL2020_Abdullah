#use of list

std_list = ["abdullah","nisar","shifa","rehan","usama","ayesha"]
for x in std_list:
    print(x)
print("-----------------------\n\n")

std_list = ["abdullah","nisar","shifa","rehan","usama","ayesha"]
std_list.sort()
for x in std_list:
    print(x)
print("-----------------------\n\n")

color = ["orange", "yellow", "grey", "blue", "red"]
color.pop()
print(color)
print("-----------------------\n\n")

digits = [12, 34, 12, 4, 21, 54, 87, 19, 27, 19, 27, 89, 37, 18, 17, 29, 10, 12, 36, 89]
y = digits.count(89)
print(digits)
print(y)
print("-----------------------\n\n")

list_num = [12, 34, 65, 32]
list_num.remove(65)
print(list_num)
print("-----------------------")