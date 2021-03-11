sorting = [3,3.4,2.8,2.5,4,3.9]

endrange = len(sorting)
for i in range(0,endrange):
    for y in range(0,endrange-1):
        if(sorting[y]>sorting[y+1]):
            temp = sorting[y]
            sorting[y] = sorting[y+1]
            sorting[y+1] = temp
            print("value",sorting[y],"   ",sorting[y+1])

print(sorting)