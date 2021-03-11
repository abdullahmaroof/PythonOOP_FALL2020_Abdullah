data = input("Enter data to implement ceaserCypher:  ")
shift = int(input("Enter the value for shift: "))
for x in range(0,len(data)):
    if data[x].isupper():
        print(data[x])
    elif data[x].islower():
        print(data[x])
    elif data[x].isdecimal():
        print(data[x])
    else:
        print("space")