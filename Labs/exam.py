class computer:
    company = ""
    ram = 0
    processor = 0
    harddisk = 0
    gpu = 0
    def startcomputer(self,c,r,p,h,g):
        print("computer is being started")
        self.company = c
        self.ram = r
        self.processor = p
        self.harddisk = h
        self.gpu = g

    def __add__(self, other):
        print("creating a super computer")
        supersystem = computer()
        supersystem.company = str(self.company)+":"+str(other.company)
        supersystem.ram = self.ram + other.ram
        supersystem.processor = self.processor + other.processor
        supersystem.harddisk = self.harddisk + other.harddisk
        supersystem.gpu = self.gpu + other.gpu
        return supersystem
    def showspecification(self):
        print("company: "+str(self.company))
        print("ram: "+str(self.ram))
        print("processor: "+str(self.processor))
        print("harddisk: "+str(self.harddisk))
        print("gpu: "+str(self.gpu))

acercom = computer()
acercom.startcomputer("acer", 4, 2.5, 500, 2.0)
dell = computer()
dell.startcomputer("dell", 8, 2.8, 1000, 2.8)
asus = computer()
asus.startcomputer("asus", 12, 3.2, 1500, 3.6)
computerlist = [acercom, dell, asus]
superComputer = computerlist[0]+computerlist[1]+computerlist[2]
superComputer.showspecification()

