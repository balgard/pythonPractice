from Items import *
from Gear import *
from Potion import * 
from Weapon import *
from Spell import *
class Weapon(Items):
    name = ""
    mana = 0
    damage = 0
    critChance = 0
    critMultiplier = 0.0
    accuracy = 0.0

    def __init__(self):
        self.name = "empty"
        self.mana = 0
        self.damage = 0

    def setDetails(self, name, mana=int, damage=int, critChance=int, critMultiplier=float, accuracy=float):
        self.name = name
        self.mana = mana
        self.damage = damage
        self.critChance = critChance
        self.critMultiplier = critMultiplier
        self.accuracy = accuracy

    def description(self):
        returned = ""
        returned += "Name: " + str(self.name)
        if self.mana != int:
            returned += "\nMana: " + str(self.mana)
        if self.damage != int:
            returned += "\nDamage: " + str(self.damage)
        if self.critChance != int:
            returned += "\nChance to deal Critical damage: " + str(self.critChance) + "%"
        if self.critMultiplier != float:
            returned += "\nCritical Damage Multiplier: " + str(self.critMultiplier)
        if self.accuracy != float:
            returned += "\nAccuracy: " + str(self.accuracy)
        return returned
