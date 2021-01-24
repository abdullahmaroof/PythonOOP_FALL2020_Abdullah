#simple stack implementation by using limit
print("")
print("*******************************************************")
print("*                       Task-1                        *")
print("*                                                     *")
print("* Name: Abdullah Maroof                               *")
print("* Roll No: BAIM-F19-007                               *")
print("* Section: 3A-BSAI/BSDS                               *")
print("* Instructor: Sir Tayyab                              *")
print("*******************************************************")
print("\n\tTask: Simple implementation of stack by using pop, push, display, peak/top function")

stack_data = []
def push():
    limit = int(input("\n\t* How many value you want to enter in stack:"))
    for i in range(0,limit):
        user_value = int(input("\n\t* Enter an value: "))
        stack_data.append(user_value)
    print("\t",stack_data)

def pop():
    if not stack_data:
        print("\n\tThe list is empty")
    else:
        remove_value = stack_data.pop()
        print("\n\tThe last value from the stack is removed")
        print("\tThe value removed from stack: ", remove_value)
        print("\t",stack_data)

def display():
    print("\n\tThe values in stack are as follow:")
    print("\t",stack_data)

def peak_top():
    print("\n\tThe top value in the stack: ", stack_data[-1])

while True:
    print("\n\t* Press 1: To enter value in stack")
    print("\n\t* Press 2: To remove value in stack")
    print("\n\t* Press 3: To display values in stack")
    print("\n\t* Press 4: To display top value in stack")
    print("\n\t* Press 5: To quit from stack progran")
    press = int(input("Press a key: "))
    if press == 1:
        push()
    elif press == 2:
        pop()
    elif press == 3:
        display()
    elif press == 4:
        peak_top()
    elif press == 5:
        break
    else:
        print("\n\t* Wrong key press*")
