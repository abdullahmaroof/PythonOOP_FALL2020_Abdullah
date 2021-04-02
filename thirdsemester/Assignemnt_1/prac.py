
def mergesort(mark_list):
    if len(marks_list)>1:
        mid = len(marks_list) // 2
        left_list = marks_list[:mid]
        right_list = marks_list[mid:]

        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j <len(right_list):
            if(left_list[i]<right_list[j]):
                marks_list[k] = left_list[i]
                i +=1
            else:
                marks_list[k] = right_list[j]
                j +=1
            k +=1

        while i < len(left_list):
            marks_list[k] = left_list[i]
            k +=1
            i +=1
        while j < len(right_list):
            marks_list[k] = right_list[j]
            k +=1
            j +=1

mergesort(marks_list)
print("Merge sorting list: ",marks_list)