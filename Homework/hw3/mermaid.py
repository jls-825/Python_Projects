from enemy import *
import random as r


class mermaid(enemy):
    def __init__(self, n, h):
        super().__init__(n, h)
        self.__defense_mode = False

    def __str__(self):
        return "Eerie singing can be heard in the distance."

    def getName(self):
        return super().getName()

    #she wants to eat you
    def getDescription(self):
        return "The mermaid is pretty, but seems to have a dark secret.";

    def basicAttack(self, enemy):
        self.__defense_mode = False  # Can't defend and attack
        enemy.doDamage(r.randint(10, 17))

    def basicName(self):
        return "Trident Stab"

    def defenseAttack(self, enemy):
        self.__defense_mode = True

    def defenseName(self):
        return "Splash"

    # heals the mermaid
    def specialAttack(self, enemy):
        self.__defense_mode = False  # Can't Defend and attack
        self.__health += r.randint(8, 25)

    def specialName(self):
        return "Sing"

    def getHealth(self):
        return self.__health

    # distinguishes between attacking and defending
    def doDamage(self, damage):
        if (self.__defense_mode):
            # Half Damage
            self.__health = self.__health - (damage // 2)
        else:
            self.__health = self.__health - damage

    def resetHealth(self):
        self.__health = 200