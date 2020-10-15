# constructor overload

class University:
    Name = ""
    age = ""
    def __init__(self, uname, uage):
        print("University Chairman")
        self.Name = uname
        self.age = uage

    def intro(self):
        print("Name is ", self.Name)
        print("Age is", self.age,"\n")

class student(University):
    def __init__(self,stdname, stdage):
        self.Name = stdname
        self.age = stdage
        print("You are a student")
        self.intro()



U1 = University("Abdullah",19)
U1.intro()
std1 = student("Samiullah",20)
