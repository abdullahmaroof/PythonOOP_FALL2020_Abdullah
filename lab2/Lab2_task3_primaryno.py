# Check primiary number

print("-------------Primary number checker------------------")
enternum = int(input("Enter a number to check prime number: "))
if enternum > 1:
    for usernum in range(2,enternum):
        if enternum % 2 == 0:
            print("The enter number",enternum," is not prime number")
        else:
            print("The enter number", enternum, " is prime number")
        break
else:
    print("The enter number", enternum, " is not prime number")