def merge(list):
    size = len(list)
    if size > 1:
        leftlist = []
        rightlist = []
        for x in range(0,int(size/2)):
            leftlist.append(list[x])
        for x in range(int(size/2),size):
            rightlist.append(list[x])

        merge(leftlist)
        merge(rightlist)
        i = 0
        j = 0
        k = 0

        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                list[k] = leftlist[i]
                i += 1
            else:
                list[k] = rightlist[j]
                j += 1
            k += 1

        while i <len(leftlist):
            list[k] = leftlist[i]
            i +=1
            k +=1

        while j < len(rightlist):
            list[k] = rightlist[j]
            j += 1
            k += 1

sorting = [12,1,3,5,11,8]
merge(sorting)
print(sorting)
