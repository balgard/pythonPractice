from Items import *
from Gear import *
from Items import *
from Potion import * 
from Weapon import *
from Spell import *
class Gear(Items):
    name = ""
    armor = 0
    mana = 0
    bossCounter = False
    avoidChance = 0

    def __init__(self):
        self.name = "empty"
        self.armor = 0
        self.mana = 0
        self.bossCounter = False

    def setDetails(self, name, armor=int, mana=int, bossCounter=bool, avoidChance=int):
        self.name = name
        self.armor = armor
        self.mana = mana
        self.bossCounter = bossCounter
        self.avoidChance = avoidChance

    def description(self):
        returned = ""
        returned += "Name: " + str(self.name)
        if self.armor != int:
            returned += "\nArmor: " + str(self.armor)
        if self.mana != int:
            returned += "\nMana: " + str(self.mana)
        if self.avoidChance != int:
            returned += "\nChance to avoid damage: " + str(self.avoidChance) + "%"
        return returned