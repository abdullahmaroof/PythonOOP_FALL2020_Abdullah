def sorting(list):
    for i in range(1,len(list)):
        unsort_element = list[i]
        while list[i-1]>unsort_element and i>0:
            temp = list[i-1]
            list[i-1] = list[i]
            list[i] = temp
            print(list[i])
            print(list[i - 1])
            print("index:",i)
            i = i-1


sort = [12,3,1,45,23,11]
sorting(sort)
print(sort)
