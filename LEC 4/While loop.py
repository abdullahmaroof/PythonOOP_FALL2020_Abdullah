# while loop practice

x = 1
while x<=10:
    i = 2*x
    print(i)
    x+=1
print("-------------------------------------------\n")

#table by using whilw loop

table = 8
i = 1
while i<=10:
    x = table * i
    print(table," * ",i," = ",x)
    i += 1
print("-------------------------------------------\n")

#nested while loop

h = 20
i = 1
while i<=4:
    j=1
    print("_____________________")
    while j<=5:
        print(h)
        h +=5
        j +=1
    i += 1