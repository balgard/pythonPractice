from Gear import *
from Items import *
from Potion import * 
from Weapon import *
from Spell import *
class Spell(Items):
    name = ""
    mana = 0
    damage = 0
    health = 0
    armor = 0
    attack = 0
    turnsBurning = 0
    turnsFrozen = 0
    turnsStunned = 0
    turnsBuffed = 0
    turnsCast = 0  # enemy spells
    cooldown = 0  # warrior spells
    hasBeenCast = False  # use with turnsCast spells
    stamina = 0  # use with rogue spells
    accuracy = 0.0
    critChance = 0
    critMultiplier = 0.0

    def __init__(self):
        self.name = "empty"
        self.mana = 0
        self.damage = 0

    def setDetails(self, name, mana=int, damage=int, health=int, armor=int, attack=int, turnsB=int, turnsF=int,
                   turnsS=int, turnsBuffed=int, turnsCast=int, cooldown=int, hasBeenCast=bool, stamina=int,
                   accuracy=float, critChance=int, critMultiplier=float):
        self.name = name
        self.mana = mana
        self.damage = damage
        self.health = health
        self.armor = armor
        self.attack = attack
        self.turnsBurning = turnsB
        self.turnsFrozen = turnsF
        self.turnsStunned = turnsS
        self.turnsBuffed = turnsBuffed
        self.turnsCast = turnsCast
        self.cooldown = cooldown
        self.hasBeenCast = hasBeenCast
        self.stamina = stamina
        self.accuracy = accuracy
        self.critChance = critChance
        self.critMultiplier = critMultiplier

    def description(self):
        returned = ""
        returned += "Name: " + str(self.name)
        if self.mana != int:
            returned += "\nMana: " + str(self.mana)
        if self.damage != int:
            returned += "\nDamage: " + str(self.damage)
        if self.health != int:
            returned += "\nHealing: " + str(self.health)
        if self.armor != int:
            returned += "\nArmor Change: " + str(self.armor)
        if self.attack != int:
            returned += "\nAttack Change: " + str(self.attack)
        if self.turnsBurning != int:
            returned += "\nBurning Turns: " + str(self.turnsBurning)
        if self.turnsFrozen != int:
            returned += "\nFrozen Turns: " + str(self.turnsFrozen)
        if self.turnsStunned != int:
            returned += "\nStunned Turns: " + str(self.turnsStunned)
        if self.turnsBuffed != int:
            returned += "\nTurns Buffed: " + str(self.turnsBuffed)
        if self.turnsCast != int:
            returned += "\nTurns Cast: " + str(self.turnsCast)
        if self.cooldown != int:
            returned += "\nCooldown: " + str(self.cooldown)
        if self.hasBeenCast != bool:
            returned += "\nHas Been Cast: " + str(self.hasBeenCast)
        if self.stamina != int:
            returned += "\nStamina Change: " + str(self.stamina)
        if self.accuracy != float:
            returned += "\nAccuracy: " + str(self.accuracy)
        if self.critChance != int:
            returned += "\nChance to Crit: " + str(self.critChance)
        if self.critMultiplier != float:
            returned += "\nCrit Multiplier: " + str(self.critMultiplier)
        return returned