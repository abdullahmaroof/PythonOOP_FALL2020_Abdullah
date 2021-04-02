data = input("Enter data to implement ceaserCypher:  ")
shift = int(input("Enter the value for shift: "))
newdata = ""
for x in data:
    if x.islower():
        if (ord(x) + shift) <= 122:
            e = chr(ord(x) + shift)
            newdata = newdata + e
        else:
            e = chr((ord(x) + shift) - 122 + 97)
            newdata = newdata + e
    elif x.isupper():
        if (ord(x)+shift) <= 90:
            e = chr(ord(x) + shift)
            newdata = newdata + e
        else:
            e = chr((ord(x)+shift)-90+64)
            newdata = newdata + e
    elif x.isdecimal():
        if (int(x)+shift) <= 9:
            e = int(x) + shift
            newdata = newdata + str(e)
        else:
            e = (int(x)+shift)-9
            newdata = newdata + str(e)
    else:
        newdata = newdata + x

print(newdata)