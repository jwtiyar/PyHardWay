from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print("This scene is not configred")

class CentralCorridor(Scene):
    def enter(self):
        print("eme central xorridjfe")

        blle = input("brro bo laser: ")

        if blle == "brro bo laser":
            return "laser_weapon_armory"
        elif blle == "hezely":
            return "death"
        else:
            print("Serkewtw nebww")
            return 'central_corridor'

class Death(Scene):
    quips = [
        "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
    ]
    def enter(self):
        print(Death.quips[randint(0, 4)])
        
class LaserWeaponArmory(Scene):
    def enter(self):
        print("Eme laser armory clas code daxl bke")
        code = '89'
        guess = input("> ")
        guesses = 0
        
        while code != guess:
            print("BizzzzzeDDD")
            exit(1)
            
        if code == guess:
            return 'the_bridge'
        else:
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print("Esta to le ser bridge chy dekey?")

        esheke = input("> ")

        if esheke == 'be swky daybne':
            return 'escape_pod'
        else:
            return 'death'
class EscapePod(Scene):
    def enter(self):
        print("Eme Escape pode")

        good_pod = "1"
        guess = input("> ")

        if guess == "1":
            return "Finished"
        else:
            return "death"

class Finished(Scene):
    def enter(self):
        print("Good Job, You Won")
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("Finished")

        while current_scene != last_scene:
            print("\n--------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Map(object):
    scenes = {'central_corridor': CentralCorridor(), 'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(), 'escape_pod': EscapePod(), 'death': Death(),
    'finished': Finished()}

    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        self.scene_name = scene_name
        destpek = Map.scenes.get(scene_name)
        return destpek
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()