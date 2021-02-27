def sorting(list):
    ran = len(list)
    if  ran<=1:
        return list
    else:
        temp = list.pop()
    lower_list = []
    greator_list = []
    for value in list:
        if(value<temp):
            lower_list.append(value)
        else:
            greator_list.append(value)
    sorting(lower_list)
    sorting(greator_list)
    for e in range(0,len(list)):
        e = list.pop()
    for elements in lower_list:
        list.append(elements)
    list.append(temp)
    for elements in greator_list:
        list.append(elements)



unsort_list = [12,11,4,1,0,8,9]
print(unsort_list)
sorting(unsort_list)
print("Quick sort: ",unsort_list)

