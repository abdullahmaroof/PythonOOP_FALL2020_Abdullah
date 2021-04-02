def quick(list):
    if len(list)<=1:
        return list
    else:
        element = list.pop()

    smalist = []
    grealist = []
    for x in list:
        if x < element:
            smalist.append(x)
        else:
            grealist.append(x)
    quick(smalist)
    quick(grealist)
    for x in range(0,len(list)):
        list.pop()
    for x in smalist:
        list.append(x)
    list.append(element)
    for x in grealist:
        list.append(x)

sort = [12,4,11,45,2,1,19]
quick(sort)
print(sort)