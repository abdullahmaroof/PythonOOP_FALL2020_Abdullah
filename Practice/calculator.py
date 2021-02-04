first_value = []
second_list = []
answer = []
first = 0
second = 0
def user():
    first = int(input("Enter first value: "))
    second = int(input("Enter second value: "))
    first_value.append(first)
    second_list.append(second)

while True:
    print("Press 1: addition\nPress 2: substraction\nPress 3: multiplication\nPress 4: divsion\nPress 5: clear memory\nPress 6: exit")
    press = int(input("Press a key 1-6: "))

    if press == 1:
        user()
        ans = first + second
        answer.append(ans)
        print("The addition: ",ans)

    elif press == 2:
        first = int(input("Enter first value: "))
        second = int(input("Enter second value: "))
        first_value.append(first)
        second_list.append(second)
        ans = first - second
        answer.append(ans)
        print("The subtraction: ", ans)

    elif press == 3:
        first = int(input("Enter first value: "))
        second = int(input("Enter second value: "))
        first_value.append(first)
        second_list.append(second)
        ans = first * second
        answer.append(ans)
        print("The multiplication: ", ans)

    elif press == 4:
        first = int(input("Enter first value: "))
        second = int(input("Enter second value: "))
        first_value.append(first)
        second_list.append(second)
        ans = first / second
        answer.append(ans)
        print("The divsion: ", ans)

    elif press == 5:
        for x in range(0,len(first_value)):
            first_value.pop()
            second_list.pop()
            answer.pop()
        print(first_value)
        print(second_list)
        print(answer)


    elif press == 6:
        break
    else:
        print("You press a wrong key")
