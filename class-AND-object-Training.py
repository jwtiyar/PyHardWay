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
person2.zanyary()


r1 = Robot("TOM", "Red", 40)
r2 = Robot("Jerry", "RED", 30)

r1.introduce()
r2.introduce()

