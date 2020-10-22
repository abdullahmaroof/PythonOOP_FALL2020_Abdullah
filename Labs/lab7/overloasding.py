class vehicle:
    no_wheel = ""
    no_lights = ""
    def intro_vehicle(self):
        print("I am simple vehicle with ", self.no_wheel," wheels")
        print("I have a ", self.no_lights," lights")

car1 = vehicle()
car1.no_wheel = 4
car1.no_lights = 8
car1.intro_vehicle()