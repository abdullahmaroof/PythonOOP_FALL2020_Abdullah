
markslist = []
file = open("marks.txt","r")
for x in file:
    markslist.append(int(x))

r= len(markslist)
for i in range(0,r-1):
    min = i
    for j in range(i,r):
        if(markslist[j]<markslist[min]):
            min = j
            temp = markslist[i]
            markslist[i] = markslist[min]
            markslist[min] = temp
print("markslist)