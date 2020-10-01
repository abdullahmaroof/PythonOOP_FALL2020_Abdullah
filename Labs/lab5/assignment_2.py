# assignment 2

print("")
print("")
print("                 Assignment-2")
print("")
print("Name: Abdullah Maroof")
print("Roll no: BAIM-F19-007")
print("\n----------------------------------------------------\n")

class animal:
    name = ""
    color = ""

    def introduceAnimal(self):
        print("Animal Name: ", self.name)
        print("Animal Color: ", self.color )
        animal.speakAnimal(self)



    def speakAnimal(self):
        if(self.name == "Jellyfish"):
            print("Seeee Seee!!!")
        elif(self.name == "Shark"):
            print("Ooooooo Oooooo!!!!")
        elif(self.name == "Dog"):
            print("wao wao!!!!!")
        elif(self.name == "Horse"):
            print("whinny whinny!!!!")
        else:
            print("Animal is not in data!!!!")


class landanimal(animal):
    def walk(self):
        print("Animal can walk on land.")


class seaanimal(animal):
    def swim(self):
        print("Animal can swim in sea.")

waterAnimal1 = seaanimal()
waterAnimal2 = seaanimal()
groundanimal1 = landanimal()
groundanimal2 = landanimal()

waterAnimal1.name = "Jellyfish"
waterAnimal1.color = "Yellow"

waterAnimal2.name = "Shark"
waterAnimal2.color = "Light-Grey"

groundanimal1.name = "Dog"
groundanimal1.color = "Black"


groundanimal2.name = "Horse"
groundanimal2.color = "Brown"

waterAnimal1.introduceAnimal()
waterAnimal1.swim()
print("------------------------------\n")
waterAnimal2.introduceAnimal()
waterAnimal2.swim()
print("------------------------------\n")
groundanimal1.introduceAnimal()
groundanimal1.walk()
print("------------------------------\n")
groundanimal2.introduceAnimal()
groundanimal2.walk()
print("------------------------------\n")
