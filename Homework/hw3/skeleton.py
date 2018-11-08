from enemy import *
import random as r


class skeleton(enemy):
    def __init__(self, n, h ):
        super().__init__(n, h)
        self.__defense_mode = False

    def __str__(self):
        return "A large sword-wielding skeleton approaches."

    def getName(self):
        return super().getName()

    def getDescription(self):
        return "A boney boy rattles before you.";

    # don't ask why the bones are infinite
    def basicAttack(self, enemy):
        self.__defense_mode = False  # Can't defend and attack
        enemy.doDamage(r.randint(8, 14))

    def basicName(self):
        return "Bone Throw"

    def defenseAttack(self, enemy):
        self.__defense_mode = True

    def defenseName(self):
        return "Shield"

    def specialAttack(self, enemy):
        self.__defense_mode = False  # Can't Defend and attack
        enemy.doDamage(r.randint(15, 18))

    def specialName(self):
        return "Sword Stab"

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
        self.__health = 150