from Gear import *
from Items import *
from Potion import * 
from Weapon import *
from Spell import *
class Potion(Items):
    name = ""
    mana = 0
    health = 0

    def __init__(self):
        self.name = "empty"
        self.mana = 0
        self.health = 0

    def setDetails(self, name, mana=int, health=int):
        self.name = name
        self.mana = mana
        self.health = health

    def description(self):
        returned = ""
        returned += "Name: " + self.name
        if self.health != int:
            returned += "\nHealth: " + str(self.health)
        if self.mana != int:
            returned += "\nMana: " + str(self.mana)
        return returned