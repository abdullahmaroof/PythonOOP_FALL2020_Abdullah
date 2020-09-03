# for loop

#simple for loop use
name = "Abdullah"
for x in range(1,8):
    print(x,": ",name)
print("------------------------------------\n")
#table in for loop
tablenum = int(input("Enter a number: "))
for table in range(1,11):
    ans = tablenum * table
    print(tablenum," * ",table," = ",ans)
print("------------------------------------\n")

#range from user
tablenum = int(input("Enter a number: "))
lower_range = int(input("Enter a number from where u want to start your table: "))
upper_range = int(input("Enter a number from where u want to end your table: "))
for table in range(lower_range,upper_range + 1):
    ans = tablenum * table
    print(tablenum, " * ", table, " = ", ans)
print("------------------------------------\n")

