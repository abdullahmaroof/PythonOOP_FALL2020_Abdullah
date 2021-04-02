sort = [12,4,6,8,22,33]
n = len(sort)

for i in range(0,n-1):
    min = i
    for j in range(i,n):
        if(sort[j]<sort[min]):
            min = j
    temp = sort[i]
    sort[i] = sort[min]
    sort[min] = temp
print(sort)