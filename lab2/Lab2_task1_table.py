# table with loops

# tbale with while loop

print("*********Table with While loop***********")


tablenum = int(input("Enter a number to get its table: "))
lowerrang = int(input("Enter start range of table: "))
upperrang = int(input("Enter end range of table: "))

while lowerrang <= upperrang:
    ans = tablenum * lowerrang
    print(tablenum," * ",lowerrang," = ",ans)
    lowerrang +=1
print("-------------------------------------------\n")

# table with for loop

print("*********Table with for loop******************")

tablenum = int(input("Enter a number to get its table: "))
lowerrang = int(input("Enter start range of table: "))
upperrang = int(input("Enter end range of table: "))
upperrang += 1
for each_num in range(lowerrang,upperrang):
    ans = tablenum*ran_
    print(tablenum," * ",ran_," = ",ans)