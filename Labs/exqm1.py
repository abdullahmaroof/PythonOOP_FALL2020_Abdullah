class Mango:
    name = ""
    size = 0
    def __add__(self, other):
        temp = self.size + other.size
        return temp
    def introduction(self):
        print("Name ",self.name)
        print("size ",self.size)

m1 = Mango()
m1.size = 10
m2 = Mango()
m2.size = 29
m3 = m1 + m2
print(type(m3))