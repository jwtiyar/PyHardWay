#Lists And Dictionaries
#Dict detwani blley detwany hemw shteky bo zyad bkey wate hemw shteky pe dekret
#wek database bekary benyt, list bynyman detwany be jmare yek be yek nawerrokekany derbkeyn bellam dict hemw shteky legellda dekret.
""" Nmwney List Eme le Interactove shell y python taqy bkerewe yan idle"""
things = ["a", "b", "c", "d"]
print(things[1])

things[1] = 'z'
print(things[1])
print(things)
# wek debynyn bo list be jmare eshy legell dekeyn.

""" Dict """

stuff = {'name': 'Jwtiyar', "age": '31', 'height': 6*15+97}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

stuff['city'] = 'Chemchemal'
print(stuff['city'])

#wek debynyt le cyaty bes jmare bekarbenyn bo bangkrdny her itemek, detwany string ysh bekarbenyn le dict.

stuff[1] = "wow"
stuff[2] = "neato"
print(stuff[1])
print(stuff[2])

#Lem dw nmwneye jmare bekarhenrawe
# Dict tenha ewe to hemw shteky bo zyad bkey bellam ewe gemjaneye, boye debet btwany shtyshy tya bsrrytewe.
print(stuff)
del stuff['age']
del stuff[1]
print(stuff)