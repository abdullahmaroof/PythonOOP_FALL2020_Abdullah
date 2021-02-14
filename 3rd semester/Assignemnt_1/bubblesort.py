markslist = []
file = open("marks.txt","r")
for x in file:
    markslist.append(int(x))

r= len(markslist)
for i in range(0,r-1):
    for j in range(0,r-i-1):
        if(markslist[j]>markslist[j+1]):
            temp = markslist[j]
            markslist[j] = markslist[j+1]
            markslist[j+1] = temp
print(markslist)
