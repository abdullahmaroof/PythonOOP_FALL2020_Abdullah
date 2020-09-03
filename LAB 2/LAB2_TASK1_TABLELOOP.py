# table with loops

# tbale with while loop

print("*********Table with While loop***********")


table = int(input("Enter a number to get its table: "))
y = int(input("Enter start range of table: "))
i = int(input("Enter end range of table: "))

while y <= i:
    x = table * y
    print(table," * ",y," = ",x)
    y +=1
print("-------------------------------------------\n")

# table with for loop

print("*********Table with for loop******************")

table = int(input("Enter a number to get its table: "))
y = int(input("Enter start range of table: "))
i = int(input("Enter end range of table: "))
i += 1
for c in range(y,i):
    x=table*c
    print(table," * ",c," = ",x)