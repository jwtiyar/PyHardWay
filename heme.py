class dame:
    def __init__(self, yekem ,dwwem):
        self.yekem = yekem
        self.dwwem = dwwem + 2
    def anjam(self):
        return (self.yekem * self.dwwem)
sht = dame(1,2)
print(sht.anjam())


class xallo(dame):
    def __init__(self, yekem, dwwem, seyem):
        super().__init__(yekem, dwwem)
        self.seyem = seyem
    def kokrdnewe(self):
        return self.yekem + self.dwwem + self.seyem
    

kone = xallo(1,2,3)

print(kone.dwwem)
