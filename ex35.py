from sys import exit

def gold_room():
    print("This room is full of gold, How much do you take? ")
    
    choice = input("> ")
    try:
        how_much = int(choice)
    except ValueError:
        dead("Man, learn to type a number.")
    
    if how_much < 50:
        print("Nice, your not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")
        
def bear_room():
    print("There is bear here")
    print("The bear has a bunch of money")
    print("the fat bear is in fornt of another door")
    print("How are you going to move the bear")
    bear_moved = False
    
    while True:
        choice = input("> ")
        
        if choice == "take money":
            dead("The bear looks at you then slaps your face")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door")
            print("You can go through it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your legs")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulu_room():
    print("Here you see the grat evil cthulu")
    print("He, it, what ever stares at you or and you go insane")
    print("Do you flee for yout life or eat your head?")
    
    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Weell that was tasty")
    else:
        cthulu_room()
    
def dead(why):
    print(why, "Good job")
    exit(0)
def start():
    print("You are in a dark room")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    
    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve")
    
start()