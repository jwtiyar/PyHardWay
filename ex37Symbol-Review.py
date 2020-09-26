


if True and True:
    print("#3 can be printed!")

bash = True
xrap = False

if bash:
    print("bashe")
elif xrap:
    print("xrape")
else:
    exit()

x = 5
print(x)
del x
x = input("> ")
try:
    x = int(x)
except ValueError:
    print("jmare bnwse")
i = 0
for i in range(5):
    print(i)

try:
    assert True, "\nA True!"  #Assert tekyd dekatewe ke shteke True e
    assert False, "\nA false!"
except AssertionError as er:
    print(er)

while True:
    print("Hi chony")
    break  #bo westandny excution lew loope.
    # eger ew break e bkeytewe continue, ewe lopp tewaw nabet her excute dekat.

class noringe():
    pass
empty = noringe()
print(empty)

class testellok:
    def __init__(self, name):
        self.name = name
        print("Robot %s initialized." % self.name)

test = testellok('robot')


try:
    perrge = open('test.txt')
    while True:
        hell = perrge.readline()
        if len(hell) == 0:
            break
        print(hell)
except KeyboardInterrupt:
    print("Key pressed")
finally:
    perrge.close()
    print("daxstny perrge")

with open('test.txt') as hell:
    print(hell.read())


def dwbarekrdnewe():
    
    return lambda x:x * 2 #Detwnyt bykey be + bellam bo esta nabet chwnke lysteke str y tedaye.
    # Lambda bekardet bo drwst krdny functioneky kwrt w xera w sade.

zyadkrdneeke = dwbarekrdnewe()
lyste = [5, 10, 15, 'hello']
print('\n Hemwy carany 2 dekret:')
for num in lyste:
    print(zyadkrdneeke(num))

#nmwneyeky tr leser lambda
x = lambda a, b: a * b  # dellet nrxy a w b m heye bellam dwatr herdwkyan carany yekdy bke.
print(x(5, 6))