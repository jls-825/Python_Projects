from enemy import *
import random as r


class giant_crab(enemy):
    def __init__(self, n, h):
        super().__init__(n, h)
        self.__defense_mode = False

    def __str__(self):
        return "An unusually large crab scuttles from the sea."

    def getDescription(self):
        return "The giant crab pinches his claws.";

    def basicAttack(self, enemy):
        self.__defense_mode = False  # Can't defend and attack
        enemy.doDamage(r.randint(5, 12))

    def basicName(self):
        return "Pinch"

    def defenseAttack(self, enemy):
        self.__defense_mode = True

    def defenseName(self):
        return "Scuttle"

    # hw charges you down with his large claw
    def specialAttack(self, enemy):
        self.__defense_mode = False  # Can't Defend and attack
        enemy.doDamage(r.randint(10, 15))

    def specialName(self):
        return "Charge"


    # distinguishes between attacking and defending
    def doDamage(self, damage):
        if (self.__defense_mode):
            # Half Damage
            super().setHealth(super().getHealth() - (damage // 2))
        else:
            super().setHealth(super().getHealth() - damage)

    def resetHealth(self):
        super().setHealth(120)