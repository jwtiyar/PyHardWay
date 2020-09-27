ten_things = "apples aranges crows telephone light sugar"
print("Wait! there are npt 10 things inside that list, let's add")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Sonf", "Frisbee", "Corn", "Banana","Girl", "Boy"]

while len(stuff) != 10:
    more_stuff.pop()
    stuff.append(more_stuff.pop())
print("there we go", stuff)

print(stuff[1])
print(stuff[-1]) #le kotayewe destpedat
print(stuff.pop()) # Lera day ekate derewe
print(''.join(stuff)) # Hemwy ekatewe tenhyshty yek be labrdny '' 
print('#'.join(stuff[3:5])) # 3 yem w 5 em wshe be yekewe dekat w # dexate newanyan wate mebesety 3 w 4 hell abzheret bes 5 naxer.