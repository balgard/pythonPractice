from Items import *
from Gear import *
from Potion import * 
from Weapon import *
from Spell import *
class Character:
    name = ""
    health = 0
    Class = ""
    mana = 0
    stamina = 0
    avoidChance = 0
    maxHealth = 0
    maxStamina = 0
    maxMana = 0
    normalAttack = 0
    inventory = []
    equipment = []
    SpellList = []
    attack = 0

    def setDetails(self, name, health, Class):
        self.name = name
        self.health = health
        self.Class = Class

    def __init__(self):
        self.name = ""
        self.health = 0
        self.Class = ""

    def display(self):
        returned = ""
        returned += "Name: " + self.name
        if self.Class != "Enemy":
            returned += "\nClass: " + self.Class
        returned += "\nHealth: " + str(self.health) + "/" + str(self.maxHealth)
        if self.maxMana != 0:
            returned += "\nMana: " + str(self.mana) + "/" + str(self.maxMana)
        if self.maxStamina != 0:
            returned += "\nStamina: " + str(self.stamina) + "/" + str(self.maxStamina)
        if self.attack != 0:
            returned += "\nDamage: " + str(self.attack) + "\nNatural Damage: " + str(self.normalAttack)
        if self.avoidChance != 0:
            returned += "\nAvoid Chance: " + str(self.avoidChance) + "%"
        return returned

    def mageClass(self):
        self.health = 100
        self.attack = 5
        self.mana = 200
        self.maxHealth = self.health
        self.maxMana = self.mana
        self.normalAttack = self.attack
        self.inventory.append(Potion())
        self.inventory[0].setDetails("Health Potion", health=50)
        self.inventory.append(Potion())
        self.inventory[1].setDetails("Mana Potion", mana=50)
        self.equipment.append(Gear())
        self.equipment[0].setDetails("Spell Tome", mana=200)
        self.equipment.append(Gear())
        self.equipment[1].setDetails("Robes", armor=10, mana=100)
        self.equipment.append(Weapon())
        self.equipment[2].setDetails("Staff", mana=100, damage=5)
        self.SpellList.append(Spell())
        self.SpellList[0].setDetails("Fireblast", damage=40, mana=30)
        self.SpellList.append(Spell())
        self.SpellList[1].setDetails("Icebolt", damage=5, mana=30, turnsF=3)
        self.SpellList.append(Spell())
        self.SpellList[2].setDetails("Combust", damage=10, mana=30, turnsB=3)
        self.SpellList.append(Spell())
        self.SpellList[3].setDetails("Lightning Shock", damage=10, turnsS=3, mana=40)

    def warriorClass(self):
        self.health = 150
        self.attack = 10
        self.maxHealth = self.health
        self.normalAttack = self.attack
        self.inventory.append(Potion())
        self.inventory.append(Potion())
        self.inventory.append(Potion())
        i = 0
        while i < len(self.inventory):
            self.inventory[i].setDetails("Health Potion", health=50)
            i += 1
        self.equipment.append(Gear())
        self.equipment[0].setDetails("Iron Armor", armor=50)
        self.equipment.append(Gear())
        self.equipment[1].setDetails("Shield", armor=10)
        self.equipment.append(Weapon())
        self.equipment[2].setDetails("Sword", damage=20)
        self.SpellList.append(Spell())
        self.SpellList[0].setDetails("Enraged", attack=20)
        self.SpellList.append(Spell())
        self.SpellList[1].setDetails("Shield Slam", damage=5, turnsS=2, cooldown=4)

    def rogueClass(self):
        self.health = 100
        self.attack = 5
        self.stamina = 200
        self.maxHealth = self.health
        self.maxStamina = self.stamina
        self.normalAttack = self.attack
        self.inventory.append(Potion())
        self.inventory.append(Potion())
        self.inventory.append(Potion())
        i = 0
        while i < len(self.inventory):
            self.inventory[i].setDetails("Health Potion", health=50)
            i += 1
        self.equipment.append(Gear())
        self.equipment[0].setDetails("Leather Armor", armor=30, avoidChance=10)
        self.equipment.append(Gear())
        self.equipment[1].setDetails("Buckler", avoidChance=10, armor=5)
        self.equipment.append(Weapon())
        self.equipment[2].setDetails("Dagger", damage=15, critChance=20, critMultiplier=2.0)
        self.SpellList.append(Spell())
        self.SpellList[0].setDetails("Backstab", damage=30, stamina=50, critChance=10, critMultiplier=2.0)
        self.SpellList.append(Spell())
        self.SpellList[1].setDetails("Find Weakness", stamina=40, critChance=100, critMultiplier=3.0)
        self.SpellList.append(Spell())
        self.SpellList[2].setDetails("Assassinate", damage=150, stamina=200)
        self.avoidChance = 20

    def enemyClass(self, h, a, s, m, i, e, sp, av):
        self.health = h
        self.attack = a
        self.stamina = s
        self.mana = m
        self.inventory = i
        self.equipment = e
        self.SpellList = sp
        self.maxHealth = h
        self.maxStamina = s
        self.maxMana = m
        self.avoidChance = av
        self.normalAttack = a