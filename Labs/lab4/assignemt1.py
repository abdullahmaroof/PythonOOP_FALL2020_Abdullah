# Assignment-1
# classes & functions
# Name: Abdullah Maroof
# Roll no: BAIM-F19-007

# Task-1: Create two classes university and teacher,
print("\n\n------------------------- Task-1 --------------------------\n")

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
print("\n\n------------------------- Task-2 --------------------------\n")

#Create 2 lists one list will contain the 5 objects of university class and second list will contain the 5 objects of teacher class.
#Then use loops to get the information and introduction of universities and teachers.

# Univeristy data

#uni1 data
univertydata1 = university
univertydata1.uniName = "Oxford University"
univertydata1.uniCity = "London"
univertydata1.uniAge = 100

#uni2 data
univertydata2 = university
univertydata2.uniName = "Superior University"
univertydata2.uniCity = "Lahore"
univertydata2.uniAge = 30

#uni3 data
univertydata3 = university
univertydata3.uniName = "Education University"
univertydata3.uniCity = "Lahore"
univertydata3.uniAge = 80

#uni4 data
univertydata4 = university
univertydata4.uniName = "NUST University"
univertydata4.uniCity = "Islamabad"
univertydata4.uniAge = 150

#uni5 data
univertydata5 = university
univertydata5.uniName = "Cambridge University"
univertydata5.uniCity = "Newyork"
univertydata5.uniAge = 120

uniDetails = [univertydata1, univertydata2, univertydata3, univertydata4, univertydata5]

for data in uniDetails:
    data.uniInformation(self=university)

print("\n------------------------------------------------------------------------")
#teachers data

#teacher1
tchdata1 = teacher
tchdata1.tchName = "Abdullah Maroof"
tchdata1.tchSubject = "Advance web development"
tchdata1.tchSal = 50000

#teacher2
tchdata2 = teacher
tchdata2.tchName = "Nisar Akram"
tchdata2.tchSubject = "OOP"
tchdata2.tchSal = 40000

#teacher3
tchdata3 = teacher
tchdata3.tchName = "Qasim Raiz"
tchdata3.tchSubject = "Artifical Intelligence"
tchdata3.tchSal = 80000

#teacher4
tchdata4 = teacher
tchdata4.tchName = "Aneesa Ashraf"
tchdata4.tchSubject = "English"
tchdata4.tchSal = 30000

#teacher5
tchdata5 = teacher
tchdata5.tchName = "Daniyal Gulzar"
tchdata5.tchSubject = "German Language"
tchdata5.tchSal = 30000

teacherdetail = [tchdata1, tchdata2, tchdata3, tchdata4, tchdata5]

for data in teacherdetail:
    data.tchintroduction(self=teacher)
print("\n------------------------------------------------------------------------")