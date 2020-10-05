class Robot(object):
    zyadkrdny_kesh2 = 1.04

    def __init__(self, name, color, wight):
        self.name = name
        self.color = color
        self.wight = wight
        

    def introduce(self):
        print("My name is", self.name, "My wight is", self.wight)

    def zyadkrdny_kesh(self):
        self.wight = self.wight * self.zyadkrdny_kesh2
        

class Person(object):
    jmarey_karmend = 0

    def __init__(self, name, personlaity, isSitting):
        self.name = name
        self.personlaity = personlaity
        self.isSitting = isSitting
    
        Person.jmarey_karmend += 1
    

    def sit_down(self):
        self.isSitting = True
    def stand_up(self):
        self.isSitting = False

    def zanyary(self):
        print(self.name, "ewey xrape", self.personlaity, "dekat", "Aye da denyshet?", self.isSitting)

class Taze(Person): #Inheritances
    zyadkrdny_kesh2 = 1.10 
#print(help(Taz)) #Bekardet bo zanyny nawerrok ew shtey detewet wek class

# Lere 0 e chwnke hy4 kareky encam nedawe 
print(Person.jmarey_karmend)
print("-" * 10)

#person1 = Person("hama", "zorqse", False)
#person2 = Person("Gazi", "kemqse", True)
print("Swd wergrtn le inheritance wate bekarhenany Person ")
person1 = Taze("hama", "zorqse", False)
person2 = Taze("Gazi", "kemqse", True)

person1.zanyary()
person2.zanyary() #Bem sheweye detwany encamy bdeyt be ewey instance y () y bdeyte chwnke xoy dyarye ke bes instance y person2 werdegret
#bellam bo ewey xwarewe:

print("-" * 10)

Person.zanyary(person1) #Lere debet instance y bdeyne chwnke class man bangkrdwa, class ysh chend method eky tedaye ke debet pey blleyt
#kame print bkat bo nmwne wtwmane person1 bere be instance.
Person.zanyary(person2)

r1 = Robot("TOM", "Red", 40)
r2 = Robot("Jerry", "RED", 30)

print("-" * 10)


r1.zyadkrdny_kesh2 = 1.05

print(Robot.zyadkrdny_kesh2) # Encamy eme her 1.04 derdechet chwnke le class awa penase krawe
print(r1.zyadkrdny_kesh2) # Bellam bo eme gorrawe chwnke eme bo r1 nrxekeman gorrywe bo 1.05
print(r2.zyadkrdny_kesh2) # Wek debyny lere nrxeke nagorret chwnke her ewey class e serekyeke werdegretewe.

print("-" * 10)

# Be __dict__ detwanyn hemww ew nrxaney heye pyshanyan bdeyn
print(r1.__dict__)
print(r2.__dict__)

print("-" * 10)

r1.introduce()
r2.introduce()

print("-" * 10)

print(r1.wight)
r1.zyadkrdny_kesh()
print(r1.wight)

print("-" * 10)

print(Person.jmarey_karmend)
