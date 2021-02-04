number = int(input("Enter a value: "))
x = number
y=0
while(number>0):
    z=number%10
    y=y*10+z
    number=number//10
if(x==y):
    print("This value is palindrome")
else:
    print("This value is not palindrome")