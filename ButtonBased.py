from tkinter import *
from characterClasses import *
from Gear import *
from Items import *
from Potion import * 
from Weapon import *
from Spell import *

root = Tk()
root.title("Kroz")
root.withdraw()
nextBattle = ""
lastBattle = ""
battleList = []
battleList.append("Tutorial Battle")
battleList.append("Second Tutorial")
# dev test branch


char = Character()



class gameScreen:
    def __init__(self, master):
        root.update()
        root.deiconify()
        self.frame = Frame(master)
        self.frame.pack()
        self.button = Button(self.frame, text="Start", command=self.start)
        self.button.pack(side=LEFT)

    def mageSelected(self, mage, warrior, rogue):
        mage.destroy()
        warrior.destroy()
        rogue.destroy()
        char.Class = "mage"
        char.mageClass()
        self.frame.pack_forget()
        details = detailsScreen(root)

    def start(self):
        self.button.destroy()
        nameField = Label(self.frame, text="Name: ")
        nameField.pack(side=LEFT)
        entryField = Entry(self.frame)
        entryField.pack(side=LEFT)
        okay = Button(self.frame, text="Confirm", command=lambda: self.okaySelected(nameField, okay, entryField))
        okay.pack(side=LEFT)

    def warriorSelected(self, warrior, mage, rogue):
        warrior.destroy()
        mage.destroy()
        rogue.destroy()
        char.Class = "warrior"
        char.warriorClass()
        self.frame.pack_forget()
        details = detailsScreen(root)

    def rogueSelected(self, rogue, mage, warrior):
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
        mage = Button(self.frame, text="Mage", command=lambda: self.mageSelected(mage, warrior, rogue))
        mage.pack(side=LEFT)
        warrior = Button(self.frame, text="Warrior", command=lambda: self.warriorSelected(warrior, mage, rogue))
        warrior.pack(side=LEFT)
        rogue = Button(self.frame, text="Rogue", command=lambda: self.rogueSelected(rogue, mage, warrior))
        rogue.pack(side=LEFT)


class detailsScreen:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.resetScreen()

    def detailsSelected(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        label = Label(self.frame, text=char.display())
        label.pack(side=TOP)
        resetButton = Button(self.frame, text="Return", command=self.resetScreen)
        resetButton.pack(side=TOP)

    def inventorySelected(self):
        self.showNewButtons(char.inventory)

    def equipmentSelected(self):
        self.showNewButtons(char.equipment)

    def spellsSelected(self):
        self.showNewButtons(char.SpellList)

    def resetScreen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        charButton = Button(self.frame, text="Character Details", command=self.detailsSelected)
        charButton.pack(side=TOP)
        inventory = Button(self.frame, text="Show Inventory", command=self.inventorySelected)
        inventory.pack(side=TOP)
        equipment = Button(self.frame, text="Show Equipment", command=self.equipmentSelected)
        equipment.pack(side=TOP)
        spells = Button(self.frame, text="Show Spells", command=self.spellsSelected)
        spells.pack(side=TOP)
        beginGame = Button(self.frame, text="Start Tutorial", command=self.startGame)
        beginGame.pack(side=TOP)

    def showNewButtons(self, selection=list):
        for widget in self.frame.winfo_children():
            widget.destroy()
        x = 0
        while x < len(selection):
            self.createNewButton(selection[x], selection)
            x += 1
        resetButton = Button(self.frame, text="Return", command=self.resetScreen)
        resetButton.pack(side=TOP)

    def showDescription(self, item, selection):
        for widget in self.frame.winfo_children():
            widget.destroy()
        label = Label(self.frame, text=item.description())
        label.pack(side=TOP)
        resetButton = Button(self.frame, text="Return", command=lambda: self.showNewButtons(selection=selection))
        resetButton.pack(side=TOP)

    def createNewButton(self, selection, selectedList):
        button = Button(self.frame, text=selection.name, command=lambda: self.showDescription(selection, selectedList))
        button.pack(side=TOP)

    def startGame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.pack_forget()
        battleScreen(root)


class battleScreen:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        td = Character()

        # Need if statement that varies based on the encounter so that this can be used for all fights
        td.Class = "Enemy"

        td.name = "Training Dummy"
        inventory = []

        td.enemyClass(100, 4, 0, 0, inventory, None, None, 0)
        td.inventory.append(Potion())
        td.inventory[0].setDetails("Health Potion", health=50)
        label = Label(self.frame, text=td.display())
        label.pack(side=TOP)
        button = Button(self.frame, text="S")
        button.pack(side=TOP)


def start():
    TEST = gameScreen(root)
    root.mainloop()


start()
