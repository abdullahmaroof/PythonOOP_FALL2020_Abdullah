sort = [12,13,11,4,6,8]
endrange = len(sort)
for i in range(0,endrange):
    min = i
    for x in range(i,endrange):
        if sort[min]>sort[x]:
            min = x
            print("value", sort[min], "   ", sort[i])
    temp = sort[min]
    sort[min] = sort[i]
    sort[i] = temp

print(sort)
