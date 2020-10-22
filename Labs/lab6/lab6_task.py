class Fruit:
    name = ""
    color = ""
    taste = ""
    def __init__(self,fname,fcolor,ftaste):
        self.name = fname
        self.color = fcolor
        self.taste = ftaste

    def introduceFruit(self):
        print("Fruit name is ", self.name)
        print("Fruit Color", self.color)

class winterFruit(Fruit):
    def fruitTaste(self):
        print("The taste of winter fruit is ", self.taste)

    def introduceFruit(self):
        print("This is  winter fruit")
        print("Fruit name is ", self.name)
        print("Fruit Color", self.color)


class summerFruit(Fruit):
    def fruitTaste(self):
        print("The taste of summer fruit is ", self.taste)

    def introduceFruit(self):
        print("This is s summer fruit")
        print("Fruit name is ", self.name)
        print("Fruit Color", self.color)


f1 = Fruit("Banana", "Yellow", "Sweet")
f1.introduceFruit()
print("")
sf1 = summerFruit("Mango","Yellow","Sweet")
sf1.introduceFruit()
sf1.fruitTaste()
print("")
sf2 = summerFruit("Apple", "Red","Sweet")
sf2.introduceFruit()
sf2.fruitTaste()
print("")
w1 = winterFruit("Orange","Orange","Sweet")
w1.introduceFruit()
w1.fruitTaste()
print("")
w2 = winterFruit("Graps","Purple","Soar")
w2.introduceFruit()
w2.fruitTaste()


