print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5. Clear Screen")
print("6. Exit")
num1 = []
num2 = []
answer = []

while True:

    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4','5','6'):


        if choice == '1':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            num1.append()
            answer = num1 + num2
            answer.append()
            answer =print(num1, "+", num2, "=", (num1+num2))



        elif choice == '2':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            answer=print(num1, "-", num2, "=", (num1-num2))

        elif choice == '3':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            answer =print(num1, "*", num2, "=", (num1*num2))

        elif choice == '4':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            answer= print(num1, "/", num2, "=", (num1/num2))

        elif choice == '5':
            for x in range(0, len(num1)):
                num1.pop()
                num2.pop()
                answer.pop()
            print(num1)
            print(num2)
            print(answer)


        elif choice == '6':
          exit()
        else:
          print("Invalid Command")