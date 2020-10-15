class Fruit:
    name = ""
    color = ""
    def __init__(self,fname,fcolor):
        self.name = fname
        self.color = fcolor

    def introduceFruit(self):
        print("Fruit name is ", self.name)
        print("Fruit Color", self.color)

class winterFruit(Fruit):
    def fruitTaste(self, taste):
        print("The taste of sumer fruit is ", taste)

    def introduceFruit(self):
        print("Fruit name is ", self.name)
        print("Fruit Color", self.color)


class summerFruit(Fruit):
    def fruitTaste(self, taste):
        print("The taste of sumer fruit is ", taste)

    def introduceFruit(self):
        print("Fruit name is ", self.name)
        print("Fruit Color", self.color)


f1 = Fruit("Banana", "Yellow")
f1.introduceFruit()
print("")
sf1 = summerFruit("Mango","Yellow")
sf1.introduceFruit()
sf1.fruitTaste("sweeter")
print("")
sf2 = summerFruit("Apple", "Red")
sf2.introduceFruit()
sf2.fruitTaste("sweet")
print("")
w1 = winterFruit("Orange","Orange")
w1.introduceFruit()
w1.fruitTaste("sweet")
print("")
w2 = winterFruit("Graps","Soar")
w2.introduceFruit()
w2.fruitTaste("Soar")

