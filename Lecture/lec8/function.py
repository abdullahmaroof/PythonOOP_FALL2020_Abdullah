# function

def stdname():
    print("Student names")
    print("* Abdullah")
    print("* Shifa")
    print("* Rehan")
    print("* Akmal")

stdname()

def stdname(self):
    name = []
    index = 0
    for name in range(0,2):
        self.name[index] = str(input("Enter student name"))
    print(name[index])

stdname()
