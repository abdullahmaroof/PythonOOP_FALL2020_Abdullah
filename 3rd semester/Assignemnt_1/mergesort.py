marks_list = []
left_list = []
right_list = []
file = open("marks.txt","r")
for marks in file:
    marks_list.append(int(marks))
print("Marks list: ",marks_list)
n= len(marks_list)
for x in range(0,int(n/2)):
    left_list.append(marks_list[x])
for y in range(int(n/2),n):
    right_list.append(marks_list[y])
print("\nLeft list: ",left_list)
print("\nRight list: ",right_list)
for i in range(0,n-1):
    for j in range(0,len(left_list)):
        if left_list[j]<right_list[j]:
            marks_list[j] = left_list[j]
        else:
            marks_list[j] = right_list[j]


print("\n Merge list: ",marks_list)