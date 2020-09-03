# Taking num from user to get even and odd

# by for loop even number

lowerrang = int(input("Enter starting range: "))
upperrang = int(input("Enter ending range: "))
upperrang += 1
for evennum in range(lowerrang,upperrang):
    if evennum % 2 == 0:
        print(evennum)
print("\n---------------------------\n")

# by for loop odd number

lowerrang = int(input("Enter starting range: "))
upperrang = int(input("Enter ending range: "))
upperrang += 1
for oddnnum in range(lowerrang,upperrang):
    if oddnnum % 2 != 0:
        print(oddnnum)
print("\n---------------------------\n")