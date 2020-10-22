class vehicle:
    no_wheel = ""
    no_lights = ""
    def intro_vehicle(self):
        print("I am simple vehicle with ", self.no_wheel," wheels")
        print("I have a ", self.no_lights," lights")

trucktar = vehicle()
trucktar.no_wheel = 4
trucktar.no_lights = 4
trucktar.intro_vehicle()