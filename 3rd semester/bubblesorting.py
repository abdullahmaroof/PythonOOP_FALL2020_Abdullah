
sort = [12,4,14,87,45]
n= len(sort)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(sort[j]>sort[j+1]):
            temp = sort[j]
            sort[j] = sort[j+1]
            sort[j+1] = temp

print(sort)
