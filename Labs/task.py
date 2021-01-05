#by using for loop
print("checking by for loop")
even, odd = 0, 0
lowerrang = int(input("Enter start range of table: "))
upperrang = int(input("Enter end range of table: "))
upperrang +=1
for num in range(lowerrang,upperrang):
    if num%3 == 0:
        print("divide by 3",num)
        even += 1
    elif num%4 ==0:
        print("divide by 4",num)
        odd += 1
    else:
        pass

print("total numbers are ",even)
print("total even numbers are ",odd)
print("\n------------------------------\n")