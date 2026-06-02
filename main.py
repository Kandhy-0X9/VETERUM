# imports
import os
import sys
import time
import random

def clearTerminal():# Clear the terminal
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def typing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def loadingAnimation(): # loading effect
    loadingtime = 5
    for i in range(loadingtime):
        clearTerminal()
        typing("_ _ _ _ _ ")
        clearTerminal()
        time.sleep(0.2)

class Players: # Player class
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
        elif mana > 20:
            self.__mana = 20
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
    

cards = [] # List of all the cards in the game

# Card objects
fireball = Card("Fireball", 10, 0, "Burn", None, 0, 0, 5, 0)
iceSpike = Card("Ice Spike", 8, 0, "Freeze", None, 0, 0, 3, 0)
heal = Card("Heal", 0, 10, None, None, 0, 0, 2, 0)
# shield = Card("Shield", 0, 0, None, None, 0, 10, 4, 0)
manaBoost = Card("Mana Boost", 0, 0, None, None, 0, 0, 3, 5)
# dmgBoost = Card("DMG Boost", 0, 0, None, None, 5, 0, 4, 0)
# immune = Card("Immune", 0, 0, None, "Immune", 0, 0, 10, 0)

cards.append(fireball)
cards.append(iceSpike)
cards.append(heal)
# cards.append(shield)
cards.append(manaBoost)
# cards.append(dmgBoost)
# cards.append(immune)

# Player and enemy objects
player = Players("Player", 100, 10)
enemy = Players("Enemy", 100, 10)

# intro
loadingAnimation()
typing("---VETERUM---\n")
typing("\nWelcome to Veterum, a card game where you battle against your opponent using a deck of cards.\nEach card has its own unique abilities and effects.\nThe goal is to reduce your opponent's health to 0 before they do the same to you.\nGood luck!")

# Main game loop
while True: # for replayability
    while player.getHealth()>0 and enemy.getHealth()>0:
        # Give passive mana regeneration
        player.setMana(player.getMana() + 3)
        enemy.setMana(enemy.getMana() + 3)
        loadingAnimation()
        cardsInPlayerHand = random.sample(cards, 3) # Randomly select 3 cards for the player's hand
        cardsInEnemyHand = random.sample(cards, 3) # Randomly select 3 cards for the enemy's hand
        print(f"Your Health: {player.getHealth()} | Your Mana: {player.getMana()}")
        print(f"Enemy Health: {enemy.getHealth()} | Enemy Mana: {enemy.getMana()}")

        print("\nYour Hand:")# show cards in player's hand
        for i, card in enumerate(cardsInPlayerHand):
            print(f"{i+1}. {card.getName()} (Mana Cost: {card.getManaCost()})")

        # Player's turn
        selectedCard = None
        while True:
            try:
                # ask player to select a card
                choice = int(input("\nSelect a card to play (1-3) or 4 to skip turn: "))
                if choice < 1 or choice > 4:
                    typing("\nInvalid choice. Please select a card between 1 and 4.")
                    continue
                elif player.getMana() < cardsInPlayerHand[choice-1].getManaCost():
                    typing("\nNot enough mana to play this card. Please select a different card.")
                    continue
                elif choice == 4:
                    typing("\nYou skipped your turn.")
                    break
                else:
                    selectedCard = cardsInPlayerHand[choice-1]
                    player.setMana(player.getMana() - selectedCard.getManaCost())
                    typing(f"\nYou played {selectedCard.getName()}!")
                    break
            except ValueError:
                typing("\nInvalid input. Please enter a number between 1 and 4.")
                continue

        # Apply card effects
        if selectedCard:
            enemy.setHealth(enemy.getHealth() - selectedCard.getDmgValue())
            player.setHealth(player.getHealth() + selectedCard.getHpRegen())
            player.setMana(player.getMana() + selectedCard.getManaBonus())

        # Enemy's turn
        playableEnemyCards = []
        for card in cardsInEnemyHand:
            if card.getManaCost() <= enemy.getMana():
                playableEnemyCards.append(card)
                
        if playableEnemyCards:
            enemyCard = random.choice(playableEnemyCards)
            enemy.setMana(enemy.getMana() - enemyCard.getManaCost())
            typing(f"\nEnemy played {enemyCard.getName()}!")

            # Apply card effects
            player.setHealth(player.getHealth() - enemyCard.getDmgValue())
            enemy.setHealth(enemy.getHealth() + enemyCard.getHpRegen())
            enemy.setMana(enemy.getMana() + enemyCard.getManaBonus())
        else:
            typing("\nEnemy has no cards to play and skips the turn.")

    # Check for win/loss conditions
    if player.getHealth() <= 0 and enemy.getHealth() <= 0:
        typing("\nIt's a draw!")
    elif player.getHealth() <= 0:
        typing("\nYou have been defeated!")
    else:
        typing("\nYou have won!")
    # game loop
    repeat = input("\nDo you want to play again? (y/n): ").strip().lower()
    if repeat == 'y':
        player.setHealth(100)
        player.setMana(10)
        enemy.setHealth(100)
        enemy.setMana(10)
    else:
        typing("\nThanks for playing! Goodbye!")
        break # outer most loop
