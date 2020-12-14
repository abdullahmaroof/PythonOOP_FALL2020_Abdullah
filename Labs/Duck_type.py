class std1():
    def intro(self):
        print("Abdullah is a student.")
    def parent(self):
        print("Abdullah has parents.")

class std2():
    def intro(self):
        print("Ali is student like Abdullah.")
    def parent(self):
        print("Ali has parents like Abdullah")

def mangofunction(o):
    o.intro()
    o.parent()

student1 = std1()
student2 = std2()

mangofunction(student1)
mangofunction(student2)
