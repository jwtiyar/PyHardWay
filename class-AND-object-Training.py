class Robot(object):
    def __init__(self, name, color, wight):
        self.name = name
        self.color = color
        self.wight = wight

    def introduce(self):
        print("My name is", self.name)

class Person(object):
    def __init__(self, name, personlaity, isSitting):
        self.name = name
        self.personlaity = personlaity
        self.isSitting = isSitting
    

    def sit_down(self):
        self.isSitting = True
    def stand_up(self):
        self.isSitting = False

    def zanyary(self):
        print(self.name, "ewey xrape", self.personlaity, "dekat", "Aye da denyshet?", self.isSitting)
        

person1 = Person("hama", "zorqse", False)
person2 = Person("Gazi", "kemqse", True)

person1.zanyary()
person2.zanyary() #Bem sheweye detwany encamy bdeyt be ewey instance y () y bdeyte chwnke xoy dyarye ke bes instance y person2 werdegret
#bellam bo ewey xwarewe:

print(Person.zanyary(person1)) #Lere debet instance y bdeyne chwnke class man bangkrdwa, class ysh chend method eky tedaye ke debet pey blleyt
#kame print bkat bo nmwne wtwmane person1 bere be instance.

r1 = Robot("TOM", "Red", 40)
r2 = Robot("Jerry", "RED", 30)

r1.introduce()
r2.introduce()

