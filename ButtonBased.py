from tkinter import *

root = Tk()
root.title("Kroz")
root.withdraw()
maxHealth = 0
maxMana = 0
maxStamina = 0
nextBattle = ""
lastBattle = ""
print("Type: start()")
class Player:
    name = ""
    health = 0
    Class = ""
    mana = 0
    stamina = 0
    avoidChance = 0
    inventory = []
    equipment = []
    spellList = []
    def setDetails(self, name, health, Class):
      self.name = name
      self.health = health
      self.Class = Class
    def __init__(self):
        self.name = ""
        self.health = 0
        self.Class = ""
    def display(self):
        print(self.name)
        print(self.health)
        print(self.Class)
    def mageClass(self):
        self.health = 100
        self.attack = 5
        self.mana = 200
        maxHealth = self.health
        maxMana = self.mana
        self.inventory.append(potion())
        self.inventory[0].setDetails("Health Potion", health=  50)
        self.inventory.append(potion())
        self.inventory[1].setDetails("Mana Potion", mana = 50)
        self.equipment.append(gear())
        self.equipment[0].setDetails("Spell Tome", mana= 200)
        self.equipment.append(gear())
        self.equipment[1].setDetails("Robes", armor = 10, mana = 100)
        self.equipment.append(weapon())
        self.equipment[2].setDetails("Staff", mana = 100, damage = 5)
        self.spellList.append(spell())
        self.spellList[0].setDetails("Fireblast", damage = 40, mana = 30)
        self.spellList.append(spell())
        self.spellList[1].setDetails("Icebolt", damage = 5, mana = 30, turnsF = 3)
        self.spellList.append(spell())
        self.spellList[2].setDetails("Combust", damage = 10, mana = 30, turnsB = 3)
        self.spellList.append(spell())
        self.spellList[3].setDetails("Lightning Shock", damage = 10, turnsS = 3, mana = 40)
    def warriorClass(self):
        self.health = 150
        self.attack = 10
        maxHealth = self.health
        self.inventory.append(potion())
        self.inventory.append(potion())
        self.inventory.append(potion())
        i = 0
        while i < len(self.inventory):
            self.inventory[i].setDetails("Health Potion", health = 50)
            i += 1
        self.equipment.append(gear())
        self.equipment[0].setDetails("Iron Armor", armor = 50)
        self.equipment.append(gear())
        self.equipment[1].setDetails("Shield", armor= 10)
        self.equipment.append(weapon())
        self.equipment[2].setDetails("Sword", damage = 20)
        self.spellList.append(spell())
        self.spellList[0].setDetails("Enraged", attack = 20)
        self.spellList.append(spell())
        self.spellList[1].setDetails("Shield Slam", damage = 5, turnsS = 2, cooldown = 4)
    def rogueClass(self):
        self.health = 100
        self.attack = 5
        self.stamina = 200
        maxHealth = self.health
        maxStamina = self.stamina
        self.inventory.append(potion())
        self.inventory.append(potion())
        self.inventory.append(potion())
        i = 0
        while i < len(self.inventory):
            self.inventory[i].setDetails("Health Potion", health = 50)
            i += 1
        self.equipment.append(gear())
        self.equipment[0].setDetails("Leather Armor", armor = 30, avoidChance = 10)
        self.equipment.append(gear())
        self.equipment[1].setDetails("Buckler", avoidChance = 10, armor = 5)
        self.equipment.append(weapon())
        self.equipment[2].setDetails("Dagger", damage = 15, critChance = 20, critMultiplier = 2.0)
        
char = Player()

class items:
    name = ""
    damage = 0
    mana = 0
    armor = 0
    turnsCast = 0
    description = ""
    turnsFrozen = 0
    turnsBurning = 0
    turnsStunned = 0
    turnsBuffed = 0
    atkBoost = 0
    cd = 0
    bossCounter = 0
    hasBeenCast = False
    health = 0
    mana = 0
    critChance = 0
    critMultiplier = 0.0
    avoidChance = 0
    stamina = 0
    accuracy = 0.0
    
class gear(items):
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
    def setDetails(self, name, armor = int, mana = int, bossCounter = bool, avoidChance = int):
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
                returned += "\nChance to avoid damage: " + str(self.avoidChance)
        return returned

class weapon(items):
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
    def setDetails(self, name, mana = int, damage = int, critChance = int, critMultiplier = float, accuracy = float):
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
                returned += "\nChance to deal Critical damage: " + str(self.critChance)
            if self.critMultiplier != float:
                returned += "\nCritical Damage Multiplier: " + str(self.critMultiplier)
            if self.accuracy !=float:
                returned += "\nAccuracy: " + str(self.accuracy)
        return returned

class potion(items):
    name = ""
    mana = 0
    health = 0
    def __init__(self):
        self.name = "empty"
        self.mana = 0
        self.health = 0
    def setDetails(self, name, mana = int, health = int):
        self.name = name
        self.mana = mana
        self.health = health
    def description(self):
        returned = ""
        returned += "Name: " + self.name
        if self.health != int:
            returned += "\nHealth: " + self.health
        if self.mana != int:
            returned += "\nMana: " + self.mana
        return returned

class spell(items):
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
    turnsCast = 0  #enemy spells
    cooldown = 0 #warrior spells
    hasBeenCast = False #use with turnsCast spells
    stamina = 0 #use with rogue spells
    accuracy = 0.0
    def __init__(self):
        self.name = "empty"
        self.mana = 0
        self.damage = 0
    def setDetails(self,name, mana = 0, damage = 0, health = 0, armor = 0, attack = 0, turnsB = 0, turnsF = 0, turnsS = 0, turnsBuffed = 0, turnsCast = 0, cooldown = 0, hasBeenCast = False, stamina = 0, accuracy = float):
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
                returned += "\nTurns Buffed: "+ str(self.turnsBuffed)
            if self.turnsCast != int:
                returned += "\nTurns Cast: "+ str(self.turnsCast)
            if self.cooldown != int:
                returned += "\nCooldown: " + str(self.cooldown)
            if self.hasBeenCast != bool:
                returned += "\nHas Been Cast: " + str(self.hasBeenCast)
            if self.stamina != int:
                returned += "\nStamina Change: " + str(self.stamina)
            if self.accuracy != float:
                returned += "\nAccuracy: " + str(self.accuracy)
        return returned

class gameScreen:
    def __init__(self, master):
        root.update()
        root.deiconify()
        self.frame = Frame(master)
        self.frame.pack()
        self.button = Button(self.frame, text="Start", command= self.start)
        self.button.pack(side=LEFT)
    def mageSelected(self,mage, warrior, rogue):
        mage.destroy()
        warrior.destroy()
        rogue.destroy()
        char.Class = "mage"
        char.mageClass()
        self.frame.pack_forget()
        details = detailsScreen(root)
    def start(self):
        self.button.destroy()
        entryField = Entry(self.frame)
        entryField.pack(side=LEFT)
        okay = Button(self.frame, text = "Confirm", command = lambda: self.okaySelected(okay, entryField))
        okay.pack(side=LEFT)
    def warriorSelected(self, warrior, mage,rogue):
        warrior.destroy()
        mage.destroy()
        rogue.destroy()
        char.Class = "warrior"
        char.warriorClass()
        self.frame.pack_forget()
        details = detailsScreen(root)
    def rogueSelected(self,rogue,mage,warrior):
        rogue.destroy()
        mage.destroy()
        warrior.destroy()
        char.Class = "Rogue"
        char.rogueClass()
        self.frame.pack_forget()
        details = detailsScreen(root)
    def okaySelected(self, button, field):
        button.destroy()
        name = field.get()
        field.destroy()
        char.name = name
        mage = Button(self.frame,text = "Mage", command = lambda: self.mageSelected(mage, warrior, rogue))
        mage.pack(side=LEFT)
        warrior = Button(self.frame, text = "Warrior", command = lambda: self.warriorSelected(warrior, mage, rogue))
        warrior.pack(side = LEFT)
        rogue = Button(self.frame, text = "Rogue", command = lambda: self.rogueSelected(rogue, mage, warrior))
        rogue.pack(side = LEFT)

class detailsScreen:
    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.pack()
        self.resetScreen()
    def detailsSelected(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        resetButton = Button(self.frame, text = "Details Screen", command = self.resetScreen)
        resetButton.pack(side = TOP)
    def inventorySelected(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        resetButton = Button(self.frame, text= "Details Screen", command = self.resetScreen)
        resetButton.pack(side = TOP)
    def equipmentSelected(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        test = Label(self.frame, text = char.equipment[0].description())
        test.pack(side = TOP)
        resetButton = Button(self.frame, text = "Details Screen", command = self.resetScreen)
        resetButton.pack(side = TOP)
    def resetScreen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        charButton = Button(self.frame, text = "Character Details", command = self.detailsSelected)
        charButton.pack(side= TOP)
        inventory = Button(self.frame, text = "Show Inventory", command = self.inventorySelected)
        inventory.pack(side= TOP)
        equipment = Button(self.frame, text = "Show Equipment", command = self.equipmentSelected)
        equipment.pack(side = TOP)
        
    
def start():
    TEST = gameScreen(root)
    root.mainloop()

    
    
