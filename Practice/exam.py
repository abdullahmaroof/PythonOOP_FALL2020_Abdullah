class person:
    name = ""
    age = ""
    def introduce(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class teacher(person):
    name = ""
    age = ""
    subject = ""
    def introduce(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Subject: ", self.subject)

class student(person):
    def introduce(self):
        print("I am studdent")
        print("Name: ",self.name)
        print("Age: ",self.age)

teacher1 = teacher()
teacher1.age = 34
teacher1.subject = "Physics"
teacher2 = teacher()
teacher2.name = "Akmal"
teacher2.age = 30
teacher2.subject = "Computer"
teacher3 = teacher()
teacher3.name = "Rehan"
teacher3.age = 28
teacher3.subject = "English"

allTeachers = [teacher1, teacher2, teacher3]


student1 = student()
student1.name = "Abdullah"
student1.age = 19
student2 = student()
student2.name = "Usama"
student2.age = 19
student3 = student()
student3.name = "   Nisar"
student3.age = 19

allStudents = [student1, student2, student3]

index = 0
for tech in allTeachers:
    allTeachers[index].introduce()
    index = index + 1
    print("------------------------")

print("\n\n")
index = 0
for std in allStudents:
    allStudents[index].introduce()
    index = index + 1
    print("------------------------")