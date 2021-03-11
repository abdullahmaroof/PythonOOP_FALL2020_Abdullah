sort = [12,4,1,44,12,13,7]
endrange = len(sort)
for x in range(1,endrange):
    element = sort[x]
    while sort[x-1] > element and x>0:
        temp = sort[x-1]
        sort[x-1] = element
        sort[x] = temp
        x -= 1
print(sort)