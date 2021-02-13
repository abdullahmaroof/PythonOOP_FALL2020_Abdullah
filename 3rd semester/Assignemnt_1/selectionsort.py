#get data from file
marks_list = []
file = open("marks.txt","r")
for marks in file:
    marks_list.append(int(marks))
print("Marks list: ",marks_list)
n= len(marks_list)
#bubblesort
for i in range(0,n-1):
    min = i
    for j in range(i,n):
        if(marks_list[j]<marks_list[min]):
            min = j
    temp = marks_list[i]
    marks_list[i] = marks_list[min]
    marks_list[min] = temp
print("\nSelection sorted list: ",marks_list)