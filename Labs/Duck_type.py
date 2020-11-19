class duck():
    def quack(self):
        print("The duck quacks")
    def swim(self):
        print("The duck swims")

class hen():
    def quack(self):
        print("The hen quacks like a duck")
    def swim(self):
        print("The hen swims like a duck")

def mangofunction(o):
    o.quack()
    o.swim()

d1 = duck()
h1 = hen()

mangofunction(d1)
mangofunction(h1)