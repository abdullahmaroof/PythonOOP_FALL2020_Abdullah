# conditions decision making

#if

marks = 80
if marks >=50:
    print("Ali is pass")
    print(marks," out of 100")
print("----------------------")

#if-else

grade = "B+"
if grade == "A+" or grade == "A-" or grade == "B+":
    print("Ali is pass")
else:
    print("Ali is fail")
print("----------------------")

#if-else-if

Agrade = "B-"
if Agrade == "A+":
    print("Ammad is pass. Grade is ",Agrade)
elif Agrade == "A-":
    print("Ammad is pass. Grade is ",Agrade)
elif Agrade == "B+":
    print("Ammad is pass. Grade is ",Agrade)
elif Agrade == "B":
    print("Ammad is pass. Grade is ",Agrade)
elif Agrade == "B-":
    print("Ammad is pass. Grade is ",Agrade)
else:
    print("Ammad is fail. Grade is ",Agrade)
print("----------------------")

#nested-if

Hgrade = "C-"
if Hgrade == "A+" or Hgrade == "A-" or Hgrade == "B+" or Hgrade == "B" or Hgrade == "B-" or Hgrade == "C+" or Hgrade == "C" or Hgrade == "C-" or Hgrade == "D":
    if Hgrade == "A+":
        print("Sami is pass. Grade is ", Hgrade,". The gpa is 4.00")
    elif Hgrade == "A-":
        print("Sami is pass. Grade is ", Hgrade, ". The gpa is 3.66")
    elif Hgrade == "B+":
        print("Sami is pass. Grade is ", Hgrade, ". The gpa is 3.33")
    elif Hgrade == "B":
        print("Sami is pass. Grade is ", Hgrade, ". The gpa is 3.00")
    elif Hgrade == "B-":
        print("Sami is pass. Grade is ", Hgrade, ". The gpa is 2.66")
    elif Hgrade == "C+":
        print("Sami is pass. Grade is ", Hgrade, ". The gpa is 2.33")
    elif Hgrade == "C":
        print("Sami is pass. Grade is ", Hgrade, ". The gpa is 2.00")
    elif Hgrade == "C-":
        print("Sami is pass. Grade is ", Hgrade, ". The gpa is 1.66")
    else:
        print("Sami is pass. Grade is ", Hgrade, ". The gpa is 1.00")
else:
    print("Sami is pass. Grade is F. The gpa is 0.00")
print("----------------------")