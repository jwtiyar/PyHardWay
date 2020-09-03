print(""" You Enter a dark room with two doors.
      Do you go through #1 or #2?""")
door = input("> ")

if door == '1':
    print("there is a giant bear here eating cheese cake")
    print("What do yo do?")
    print("1. take the cake")
    print("2. Scream at the bear")
    bear = input("> ")
    if bear == '1':
        print("Bear eats ypur face off.")
    elif bear == "2":
        print("The bear eats your legs off")
    else:
        print(f"well, doing {bear} id probablt better.")
        print("Bear runs away")
        
elif door == "2":
    print("You stare into endless abyss at Cthulhu retina")
    print("1. Blueberries")
    print("2. Yellow a=jacket clothespin")
    print("3. Understanding revolvers yelling")
    insanity = input("> ")
    if insanity == "1": # or insanity == "2":ثؤؤثؤ
        print("Your body survives powered by mind of jello")
        print("Good Job")
    elif  insanity == "2":
        print("Yellow")
    else:
        print("THE instanity rots your eyes")
        print("Good job")
else:
    print("You stumble around and fall on a knife and die. good job")