# Assignment-1
# classes & functions
# Name: Abdullah Maroof
# Roll no: BAIM-F19-007

# Task-1: Create two classes university and teacher,
print("\n\n-------------------------Task-1--------------------------\n")

# University class will have three variable ---> uniName, uniCity, uniAge
# University class will have one function ---> University Information ---> which will show all the information of university.

class university:
    uniName = ""
    uniCity = ""
    uniAge = ""

    def uniInformation(self):
        print("---------Univerity Information-----------\n")
        print("* University Name: ", self.uniName)
        print("* University City: ", self.uniCity)
        print("* University Age: ", self.uniAge,"year old")
        print("--------------------------------------------------")

univertydata = university
univertydata.uniName = "Oxford University"
univertydata.uniCity = "London"
univertydata.uniAge = 100
univertydata.uniInformation(self=university)

# Teacher class will have three variable ---> tchName, tchSubject, tchSal
# Teacher class will have one function ---> Teacher Introduction ---> which will show the introduction of teacher.

class teacher:
    tchName = ""
    tchSubject = ""
    tchSal = ""

    def tchintroduction(self):
        print("\n\n---------Teacher Introduction-----------\n")
        print("* Teacher Name: ", self.tchName)
        print("* Teacher Subject: ", self.tchSubject)
        print("* Teacher Sallery: ", self.tchSal,"RS")
        print("--------------------------------------------------")

tchdata = teacher
tchdata.tchName = "Abdullah Maroof"
tchdata.tchSubject = "Advance web development"
tchdata.tchSal = 50000
tchdata.tchintroduction(self=teacher)

#task2
print("\n\n-------------------------Task-1--------------------------\n")

#Create 2 lists one list will contain the 5 objects of university class and second list will contain the 5 objects of teacher class.
#Then use loops to get the information and introduction of universities and teachers.
