# simple inheritance

class svl:
    name = ""
    section = ""

    def intro(self):
        print("Intro of SVL")
        print("Name: " + self.name)
        print("Section: " + self.section)
        print("------------------------------\n")

class student:
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