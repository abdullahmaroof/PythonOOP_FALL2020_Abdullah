# Taking num from user to check even and odd

#check even number
print("**********Q1 start******************")
print("check number enetered by user is even or odd ")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number enetered by user is even and number is ",num)
else:
    print("The number enetered by user is odd and number is ", num)
print("\n------------------------------")
print("**********Q1 END******************\n\n")


#Check which number is odd and even in range
print("Check which is odd and even in range")

#by using for loop
print("**********Q2 start******************")
print("checking by for loop")
lowerrang = int(input("Enter start range of table: "))
upperrang = int(input("Enter end range of table: "))
upperrang = +1
for eachnum in range(lowerrang,upperrang):
    if eachnum %2 == 0:
        print("The number is even: ",eachnum)
    else:
        print("The number is odd: ", eachnum)
print("\n------------------------------")
print("**********Q2 END******************\n\n")

#by using while loop
print("**********Q3 start******************")
print("checking by while loop")
lowerrang = int(input("Enter start range of table: "))
upperrang = int(input("Enter end range of table: "))
while lowerrang <= upperrang:
    if lowerrang %2 == 0:
        print("The number is even: ",lowerrang)
    else:
        print("The number is odd: ", lowerrang)
    lowerrang += 1
print("\n------------------------------\n")
print("**********Q3 END******************\n\n")


#check how many number are odd and even in range
print("**********Q4 start******************")
print("Check how many numbers are even and odd in range and range entered by user")

#by using for loop
print("checking by for loop")
even, odd = 0, 0
lowerrang = int(input("Enter start range of table: "))
upperrang = int(input("Enter end range of table: "))
upperrang +=1
for num in range(lowerrang,upperrang):
    if num%3 == 0:
        even += 1
    else:
        odd += 1
print("total numbers are ",even)
print("total even numbers are ",odd)
print("\n------------------------------\n")

#by using while loop
print("checking by while loop")
even, odd = 0, 0
lowerrang = int(input("Enter start range of table: "))
upperrang = int(input("Enter end range of table: "))

while lowerrang<=upperrang:
    if lowerrang%2 == 0:
        even += 1
    else:
        odd += 1
    lowerrang +=1
print("total even numbers are ",even)
print("total even numbers are ",odd)
print("\n------------------------------")
print("**********Q4 END******************\n\n")
