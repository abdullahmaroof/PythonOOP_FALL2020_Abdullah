marks_list = []
file = open("marks.txt","r")
for marks in file:
    marks_list.append(int(marks))
print("Marks list: ",marks_list)
n= len(marks_list)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(marks_list[j]>marks_list[j+1]):
            temp = marks_list[j]
            marks_list[j] = marks_list[j+1]
            marks_list[j+1] = temp
print("\nBubble sorted list: ",marks_list)
