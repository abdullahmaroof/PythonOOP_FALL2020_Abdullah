class vehicle:
    no_wheel = ""
    no_lights = ""
    def intro_vehicle(self):
        print("I am simple vehicle with ", self.no_wheel," wheels")
        print("I have a ", self.no_lights," lights")
    def __add__(self, other):
        temp1 = self.no_wheel + other.no_wheel
        temp2 = self.no_lights + other.no_lights
        return [temp1, temp2]

trucktar = vehicle()
trucktar.no_wheel = 4
trucktar.no_lights = 4
trucktar.intro_vehicle()

tarali = vehicle()
tarali.no_wheel = 2
tarali.no_lights = 2
tarali.intro_vehicle()

totalv = vehicle()
totalv = trucktar + tarali
print(totalv)

