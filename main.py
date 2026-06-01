# imports
import os
import sys
import time

def clearTerminal():# Clear the terminal
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



class Player: # Player class
    def __init__(self, name, health, mana):
        self.__name = name
        self.__health = health
        self.__mana = mana
    # Getters
    def getName(self):
        return self.__name
    def getHealth(self):
        return self.__health
    def getMana(self):
        return self.__mana
    
    # Setters
    def setHealth(self, health):
        if health < 0:
            self.__health = 0
        else:
            self.__health = health
    def setMana(self, mana):
        if mana < 0:
            self.__mana = 0
        else:
            self.__mana = mana

class Card: # Card class
    def __init__(self, name, dmgValue, hpRegen, debuff, buff, dmgBoost, shieldValue, manaCost, manaBonus):
        self.__name = name
        self.__dmgValue = dmgValue
        self.__hpRegen = hpRegen
        self.__debuff = debuff
        self.__buff = buff
        self.__dmgBoost = dmgBoost
        self.__shieldValue = shieldValue
        self.__manaCost = manaCost
        self.__manaBonus = manaBonus
    # Getters
    def getName(self):
        return self.__name
    def getDmgValue(self):
        return self.__dmgValue
    def getHpRegen(self):
        return self.__hpRegen
    def getDebuff(self):
        return self.__debuff
    def getBuff(self):
        return self.__buff
    def getDmgBoost(self):
        return self.__dmgBoost
    def getShieldValue(self):
        return self.__shieldValue
    def getManaCost(self):
        return self.__manaCost
    def getManaBonus(self):
        return self.__manaBonus
    
    def __str__(self):# string representation of the card
        return f"--{self.__name}--\nDMG: {self.__dmgValue}\nHP Regen: {self.__hpRegen}\nDebuff: {self.__debuff}\nBuff: {self.__buff}\nDMG Boost: {self.__dmgBoost}\nMana Cost: {self.__manaCost}\nMana Bonus: {self.__manaBonus}"
    

CardsLibrary = [] # List of all the cards in the game

fireball = Card("Fireball", 10, 0, "Burn", None, 0, 0, 5, 0)
iceSpike = Card("Ice Spike", 8, 0, "Freeze", None, 0, 0, 3, 0)
heal = Card("Heal", 0, 10, None, None, 0, 0, 2, 0)
shield = Card("Shield", 0, 0, None, None, 0, 10, 4, 0)
manaBoost = Card("Mana Boost", 0, 0, None, None, 0, 0, 3, 5)
dmgBoost = Card("DMG Boost", 0, 0, None, None, 5, 0, 4, 0)

CardsLibrary.append(fireball)
CardsLibrary.append(iceSpike)
CardsLibrary.append(heal)
CardsLibrary.append(shield)
CardsLibrary.append(manaBoost)
CardsLibrary.append(dmgBoost)


clearTerminal()
print("---VETERUM---")
print("Welcome to Veterum, a card game where you battle against your opponent using a deck of cards.\nEach card has its own unique abilities and effects.\nThe goal is to reduce your opponent's health to 0 before they do the same to you.\nGood luck!")



print()
print()