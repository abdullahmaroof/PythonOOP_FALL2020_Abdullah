# task1 of inheritance
# multiple inheritance

class parent:
    father_name = ""
    mother_name = ""

    def motorcycle(self):
        print("This is ", self.father_name,"'s motorcyle")


class child(parent):
    child_name = ""
    child_age = ""
    def info(self):
        print("-----------------------------------")
        print("Name: ", self.child_name)
        print("Father Name: ", self.father_name)
        print("Mother Name: ", self.mother_name)
        print("Age: ", str(self.child_age)," year olf")
        print("---------------------------------")
        parent.motorcycle(self)
        print("----------------------------------")

    def __add__(self, other):
        temp = self.child_age + other.child_age
        return  temp

son = child()
son.child_name = "Abdullah"
son.father_name = "Maroof"
son.mother_name = "Shahida"
son.child_age = 20

son.info()

son2 = child()
son2.child_name = "Ali"
son2.father_name = "Maroof"
son2.mother_name = "Shahida"
son2.child_age = 25

son2.info()


son3 = child()
son3 = son + son2
print(son3)
