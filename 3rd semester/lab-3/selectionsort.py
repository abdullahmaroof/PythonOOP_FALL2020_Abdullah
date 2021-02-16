sort = []
limit = int(input("Enter the range of values: "))
for x in range(0,limit):
    v = x+1
    value = int(input("Enter a value in list= "))
    sort.append(value)
print("\nUn sort apply",sort)
n= len(sort)
for i in range(0,n-1):
    min = i
    for j in range(i,n):
        if(sort[j]<sort[min]):
            min = j
    temp = sort[i]
    sort[i] = sort[min]
    sort[min] = temp
print("\nSelection sort apply",sort)