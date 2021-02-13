def mergeSort(myList):
    if len(myList) > 1:
        left_list = []
        right_list = []
        n = len(myList)
        for x in range(0,int(n/2)):
            left_list.append(myList[x])

        for y in range(int(n/2),n):
            right_list.append(myList[y])

        print("\nLeft list: ",left_list)
        print("\nRight list: ", right_list)
        mergeSort(left_list)
        mergeSort(right_list)
        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                myList[k] = left_list[i]
                i += 1
            else:
                myList[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            myList[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            myList[k] = right_list[j]
            j += 1
            k += 1


marks_list = []
file = open("marks.txt","r")
for marks in file:
    marks_list.append(int(marks))
print("Marks list: ",marks_list)
mergeSort(marks_list)
print("\nMarks list after merge sort: ",marks_list)