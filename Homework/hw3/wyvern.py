from enemy import *
import random as r


class wyvern(enemy):
    def __init__(self, n, h):
        super().__init__(n, h)
        self.__defense_mode = False

    def __str__(self):
        return "A fiery beast swoops down from the sky."


    #he has a lot of health
    def getDescription(self):
        return "A proud beast glares at you.";

    def basicAttack(self, enemy):
        self.__defense_mode = False  # Can't defend and attack
        enemy.doDamage(r.randint(10, 18))

    def basicName(self):
        return "Gust"

    def defenseAttack(self, enemy):
        self.__defense_mode = True

    def defenseName(self):
        return "Tail Parry"

    #can potentially do a lot of damage
    def specialAttack(self, enemy):
        self.__defense_mode = False  # Can't Defend and attack
        enemy.doDamage(r.randint(5, 35))

    def specialName(self):
        return "Fireball"


    # distinguishes between attacking and defending
    def doDamage(self, damage):
        if (self.__defense_mode):
            # Half Damage
            super().setHealth(super().getHealth() - (damage // 2))
        else:
            super().setHealth(super().getHealth() - damage)

    def resetHealth(self):
        super().setHealth(200)