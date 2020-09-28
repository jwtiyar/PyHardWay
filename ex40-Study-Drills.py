import mystuff
class gorany(object):
    def __init__(self, honrawe):
        self.honrawe = honrawe
    def gornayeke_Rrek_bxe(self):
        for derr in self.honrawe:
            print(derr)
    
Honraweke = gorany(["Hende nahene", "Le dnya Xem bxoy", "Amanetyt ebet zw brroy"])
dangeke = gorany(["Hende nahene", "Le dnya Xem bxoy", "Amanetyt ebet zw brroy"])
zanyary = ["Em goranye hy Frmeske"]
Honraweke.gornayeke_Rrek_bxe()
dangeke.gornayeke_Rrek_bxe()

print("=" * 20)
zanyarekanm = gorany(zanyary)
zanyarekanm.gornayeke_Rrek_bxe()
print("=" * 20)