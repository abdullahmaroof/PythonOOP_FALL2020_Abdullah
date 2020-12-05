#this program will take input marks from user and show us the grade according to marks

print("**********************************************")
print("*         Programming Fundamental            *")
print("*             Assignment-2                   *")
print("*                                            *")
print("* Name: Noor Anwar                           *")
print("* Rollno : BDSM-F20-002                      *")
print("* Section: 1A                                *")
print("* Program: BS Data Science                   *")
print("**********************************************")
print("\n\nQ:Make a program which will take marks as an input from user and show grade?")
print("\nProgram:-")
print("\t\tRules for grading:")
print("\t\t1: A+ 90 or greater than 90")
print("\t\t2: A 80 or greater than 80 and less than 90")
print("\t\t3: B+ 70 or greater than 70 and less than 80")
print("\t\t4: B- 60 or greater than 60 and less than 70")
print("\t\t5: C+ 55 or greater than 55 and less than 60")
print("\t\t6: C 50 or greater than 50 and less than 55")
print("\t\t7: F less than 50")
name = input("\n\t\tEnter your name: ")
print("\t\t"+name+", you can check your first semester result from here.")
print("\t\tPlease enter your every subject marks. Total marks = 500")
eng_marks = int(input("\t\tTotal marks 100.Enter your marks of English Composition and Comprehension: "))
discrete_marks = int(input("\t\tTotal marks 100.Enter your marks of Discrete Structure: "))
itc_marks = int(input("\t\tTotal marks 100.Enter your marks of Introduction to Computing: "))
calculus_marks = int(input("\t\tTotal marks 100.Enter your marks of Calculus: "))
pf_marks = int(input("\t\tTotal marks 100.Enter your marks of Programming Fundamental: "))
total_marks = eng_marks + discrete_marks + itc_marks + calculus_marks + pf_marks
print("\n\t\tTotal marks "+str(total_marks)+" out of 500")
percentage = (total_marks * 100)/500
print("\t\tPercentage = "+str(percentage))
if percentage >= 90:
    print("\t\t"+name+", your grade is A+")
elif percentage >= 80:
    print("\t\t" + name + ", your grade is A")
elif percentage >= 70:
    print("\t\t" + name + ", your grade is B+")
elif percentage >= 60:
    print("\t\t" + name + ", your grade is B-")
elif percentage >= 55:
    print("\t\t" + name + ", your grade is C+")
elif percentage >= 50:
    print("\t\t" + name + ", your grade is C")
else:
    print("\t\t" + name + ", your grade is F")