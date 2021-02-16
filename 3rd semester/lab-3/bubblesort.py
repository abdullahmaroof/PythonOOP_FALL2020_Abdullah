
sort = []
limit = int(input("Enter the range of values: "))
for x in range(0,limit):
    v = x+1
    value = int(input("Enter a value in list= "))
    sort.append(value)
print("\nUn sort apply",sort)
n= len(sort)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(sort[j]>sort[j+1]):
            temp = sort[j]
            sort[j] = sort[j+1]
            sort[j+1] = temp

print("\nBubble sort apply",sort)
