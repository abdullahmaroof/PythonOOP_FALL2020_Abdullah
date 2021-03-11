x=[1,2]
def push():
    element = int(input("Enter a value in stack: "))
    print("before adding a value in stack: ", x)
    x.append(element)
    print("After adding a value in stack: ",x)
def popstack():
    element = x.pop()
    print("The element remove from stack: ", element)
    print("After removing a value in stack: ", x)

def popqueue():
    element = x.pop(0)
    print("The element remove from stack: ", element)
    print("After removing a value in stack: ", x)

def display():
    print("The stack: ",x)
while True:
    print("1: working of stack\n2: working of queue\n3: exit")
    press = int(input("press key: "))
    if press == 1:
        while True:
            print("1: insert a value\n2: delete a value\n3: display\n4: exit")
            press = int(input("press key: "))
            if press == 1:
                push()
            elif press == 2:
                popstack()

            elif press == 3:
                display()

            elif press == 4:
                break

            else:
                print("you press wrong key")

    elif press == 2:
        while True:
            print("1: insert a value\n2: delete a value\n3: display\n4: exit")
            press = int(input("press key: "))
            if press == 1:
                push()
            elif press == 2:
                popqueue()

            elif press == 3:
                display()

            elif press == 4:
                break

            else:
                print("you press wrong key")