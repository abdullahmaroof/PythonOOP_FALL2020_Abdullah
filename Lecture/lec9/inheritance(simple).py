# simple inheritance

class svl:
    name = ""
    section = ""

    def intro(self):
        print("Intro of SVL")
        print("Name: " + self.name)
        print("Section: " + self.section)
        print("------------------------------\n")

class student(svl):
    name = ""
    section = ""

cr1 = svl()
cr2 = svl()

cr1.name = "Abdullah"
cr1.section = "2A"

cr2.name = "Nisar"
cr2.section = "3D"

cr1.intro()
cr2.intro()

std1 = student()
std2 = student()

std1.name = "Usama"
std1.section = "2A"

std2.name = "Akmal"
std2.section = "3D"

std1.intro()
std2.intro()