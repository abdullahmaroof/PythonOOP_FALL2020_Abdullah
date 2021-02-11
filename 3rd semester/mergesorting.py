sort = [12,4,6,8,22,33]
n = len(sort)

for i in range(0,n-1):
    min = i
    for j in range(i+1):
        if(sort[j]>sort[min]):
            temp = sort[j]
            sort[j] = sort[min]
            sort[min] = temp

print(sort)