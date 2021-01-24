# fib = [0]
# num1= 0
# num2 = 1
# endrange = int(input("Enter range: "))
# startrange= 0
# for x in range(startrange,endrange):
#     if(num1<endrange and num2<endrange):
#         ans = num1+num2
#         fib.append(ans)
#         num2 = num1
#         num1 = ans
# fib.pop()
# print(fib)

# str1 = "How Are You Students"
# newStr = ""
#
# for i in range(0, len(str1)):
#     if str1[i].isupper():
#         newStr += str1[i].lower()
#
#     elif str1[i].islower():
#         newStr += str1[i].upper()
#
#     else:
#         newStr += str1[i]
#
# print("String after case conversion : " + newStr)


fib = [0]
num1 = 0
num2 = 1
endrange = int(input("range: "))
for i in range(0,endrange):
    if(num1<endrange and num2<endrange):
        ans = num1+num2
        fib.append(ans)
        num2 = num1
        num1 = ans
fib.pop()
print(fib)




