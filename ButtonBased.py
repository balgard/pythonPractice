from tkinter import *

root = Tk()
root.title("Kroz")
root.withdraw()
nextBattle = ""
lastBattle = ""






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
    spellList = []
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
        returned += "Name: "+ self.name
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
        self.maxHealth = self.health
        self.normalAttack = self.attack
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
        self.maxHealth = self.health
        self.maxStamina = self.stamina
        self.normalAttack = self.attack
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
        self.spellList.append(spell())
        self.spellList[0].setDetails("Backstab", damage = 30, stamina = 50, critChance = 10, critMultiplier = 2.0)
        self.spellList.append(spell())
        self.spellList[1].setDetails("Find Weakness", stamina = 40, critChance = 100, critMultiplier= 3.0)
        self.spellList.append(spell())
        self.spellList[2].setDetails("Assassinate", damage = 150, stamina = 200)
        self.avoidChance = 20
    def enemyClass(self, h, a, s, m, i, e, sp, av):
        self.health = h
        self.attack = a
        self.stamina = s
        self.mana = m
        self.inventory = i
        self.equipment = e
        self.spellList = sp
        self.maxHealth = h
        self.maxStamina = s
        self.maxMana = m
        self.avoidChance = av
        self.normalAttack = a
        
char = Character()

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
    bossCounter = False
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
                returned += "\nChance to avoid damage: " + str(self.avoidChance) + "%"
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
                returned += "\nChance to deal Critical damage: " + str(self.critChance) + "%"
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
            returned += "\nHealth: " + str(self.health)
        if self.mana != int:
            returned += "\nMana: " + str(self.mana)
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
    critChance = 0
    critMultiplier = 0.0
    def __init__(self):
        self.name = "empty"
        self.mana = 0
        self.damage = 0
    def setDetails(self,name, mana = int, damage = int, health = int, armor = int, attack = int, turnsB = int, turnsF = int, turnsS = int, turnsBuffed = int, turnsCast = int, cooldown = int, hasBeenCast = bool, stamina = int, accuracy = float, critChance = int, critMultiplier = float):
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
        if self.critChance != int:
            returned += "\nChance to Crit: " + str(self.critChance)
        if self.critMultiplier != float:
            returned += "\nCrit Multiplier: " + str(self.critMultiplier)
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
        nameField = Label(self.frame, text = "Name: ")
        nameField.pack(side = LEFT)
        entryField = Entry(self.frame)
        entryField.pack(side=LEFT)
        okay = Button(self.frame, text = "Confirm", command = lambda: self.okaySelected(nameField, okay, entryField))        
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
    def okaySelected(self, name, button, field):
        name.destroy()
        button.destroy()
        name = field.get()
        field.destroy()
        char.name = name
        if char.name == '':
            char.name = "Stranger"
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
        label = Label(self.frame, text = char.display())
        label.pack(side = TOP)
        resetButton = Button(self.frame, text = "Return", command = self.resetScreen)
        resetButton.pack(side= TOP)
    def inventorySelected(self):
        self.showNewButtons(char.inventory)
    def equipmentSelected(self):
        self.showNewButtons(char.equipment)
    def spellsSelected(self):
        self.showNewButtons(char.spellList)
    def resetScreen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        charButton = Button(self.frame, text = "Character Details", command = self.detailsSelected)
        charButton.pack(side= TOP)
        inventory = Button(self.frame, text = "Show Inventory", command = self.inventorySelected)
        inventory.pack(side= TOP)
        equipment = Button(self.frame, text = "Show Equipment", command = self.equipmentSelected)
        equipment.pack(side = TOP)
        spells = Button(self.frame, text = "Show Spells", command = self.spellsSelected)
        spells.pack(side = TOP)
        beginGame = Button(self.frame, text = "Start Tutorial", command = self.startGame)
        beginGame.pack(side=  TOP)
    def showNewButtons(self,selection = list):
        for widget in self.frame.winfo_children():
            widget.destroy()
        x = 0
        while x < len(selection):
            self.createNewButton(selection[x], selection)
            x += 1
        resetButton = Button(self.frame, text = "Return", command = self.resetScreen)
        resetButton.pack(side = TOP)
    def showDescription(self, item, selection):
        for widget in self.frame.winfo_children():
            widget.destroy()
        label = Label(self.frame, text = item.description())
        label.pack(side = TOP)
        resetButton = Button(self.frame, text = "Return", command = lambda: self.showNewButtons(selection = selection))
        resetButton.pack(side = TOP)
    def createNewButton(self, selection, selectedList):
        button = Button(self.frame, text = selection.name, command = lambda:  self.showDescription(selection, selectedList))
        button.pack(side=TOP)
    def startGame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.pack_forget()
        x = battleScreen(root)
class battleScreen:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        td = Character()
        #Need if statement that varies based on the encounter so that this can be used for all fights
        td.Class = "Enemy"
        td.name = "Training Dummy"
        inventory = []
        inventory.append(potion().setDetails("Health Potion", health = 50))
        td.enemyClass(100, 4, 0,0, inventory, None, None, 0)
        label = Label(self.frame, text = td.display())
        label.pack(side = TOP)
        button = Button(self.frame, text = "S")
        button.pack(side = TOP)
        
        
    
def start():
    TEST = gameScreen(root)
    root.mainloop()


start()
    
