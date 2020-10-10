class fruit:
    nmae = ""
    color = ""
    def showFruit(self):
        print("name of fruit ", self.nmae)
        print("color of fruit ", self.color)
    def tasteFruit(self, taste):
        print("The Fruit is", taste,"in taste")

class winterFruit(fruit):
    def tasteFruit(self):
        print("The",self.nmae," is bitter")
    def fruitType(self):
        print("This is winter fruit")
class summerfruit(fruit):
    def fruitType(self):
        print("This is summer fruit")

mango = fruit()
mango.nmae = "Mango"
mango.color = "Yellow"
mango.showFruit()
mango.tasteFruit("Sweet")
print("---------------------------------")

orange = summerfruit()
orange.nmae = "Orange"
orange.color = "Orange"
orange.fruitType()
orange.tasteFruit()
print("--------------------------------")

apple = winterFruit()
apple.nmae = "Apple"
apple.color = "Red"
apple.showFruit()
apple.tasteFruit("Sweetish")