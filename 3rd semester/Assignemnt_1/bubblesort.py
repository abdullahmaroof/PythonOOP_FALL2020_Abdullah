#get data from file
marks_list = []
file = open("marks.txt","r")
for marks in file:
    marks_list.append(marks)
print("Marks list: ",marks_list)