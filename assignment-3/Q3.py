

print("----------------------------------------------")
print("*         Programming Fundamental            *")
print("*             Assignment-3                   *")
print("*                                            *")
print("* Name: Fatima Amir                          *")
print("* Rollno : BDSM-F20-001                      *")
print("* Section: 1A                                *")
print("* Program: BS Data Science                   *")
print("----------------------------------------------")
print("\n\nQ:Make a program which we will tell next prime number?")
print("\nProgram:-")
prime = [2,3,5,7,11,13,17,19,23]
newprime = []
print("\n* prime numbers: ",prime)
ran = int(input("\n* Enter range: "))
values = int(input("* how many prime values you want to get in this range after 23(values 0 - 5): "))

for num in range(24,ran):
    if(num%2==0 or num%3==0 or num%5==0 or num%7==0):
        pass
    else:
        prime.append(num)
values = values+9

for x in range(0,values):
    newprime.append(prime[x])



print("\n* prime numbers: ",newprime)