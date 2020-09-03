# Taking num from user to get even and odd

# by for loop even number
print("even number by using for loop")
lowerrang = int(input("Enter starting range: "))
upperrang = int(input("Enter ending range: "))
upperrang += 1
for evennum in range(lowerrang,upperrang):
    if evennum % 2 == 0:
        print(evennum)
print("\n---------------------------\n")

# by for loop odd number
print("odd number by using for loop")
lowerrang = int(input("Enter starting range: "))
upperrang = int(input("Enter ending range: "))
upperrang += 1
for oddnnum in range(lowerrang,upperrang):
    if oddnnum % 2 != 0:
        print(oddnnum)
print("\n---------------------------\n")

# by while loop even number
print("even number by using whileloop")
lowerrang = int(input("Enter starting range: "))
upperrang = int(input("Enter ending range: "))

while lowerrang<=upperrang:
    if lowerrang % 2 == 0:
        print(lowerrang)
    lowerrang += 1
print("\n---------------------------\n")

# by while loop odd number
print("odd number by while for loop")
lowerrang = int(input("Enter starting range: "))
upperrang = int(input("Enter ending range: "))

while lowerrang<=upperrang:
    if lowerrang % 2 != 0:
        print(lowerrang)
    lowerrang += 1
print("\n---------------------------\n")