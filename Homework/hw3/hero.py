from enemy import *
import random as r

class hero(enemy):
    def __init__(self, n, h):
        super().__init__(n, h)
        self.__potion = 6
        self.__pot = True
        self.__fire = 10
        self.__fireball = True
        self.__defense_mode = False

    def __str__(self):
        return super().getName() + ":" + str(super().getHealth()) + "/150 health\nRemaining: " + str(self.__fire) + " Fireballs " + str(self.__potion) + " Potions"

    #its too dangerous to go alone take this
    def getDescription(self):
        return "A mysterious traveler journeys onward.";

    def basicAttack(self, enemy):
        self.__defense_mode = False  # Can't defend and attack
        enemy.doDamage(r.randint(10, 20))

    def basicName(self):
        return "Sword Slash"

    def defenseAttack(self, enemy):
        self.__defense_mode = True

    def defenseName(self):
        return "Sheild"

    #throws fireball and makes sure to get rid of one
    def specialAttack(self, enemy):
        self.__defense_mode = False  # Can't defend and attack
        if self.__fire > 0:
            self.__fireball = True
            self.__fire -= 1
            enemy.doDamage(25)
        else:
            self.__fireball = False
    def specialName(self):
        if self.__fireball:
            return "Fireball Attack"
        return "Fireball Attack Unsuccessful."

    #i need healing
    def Heal(self):
        if self.__potion > 0:
            self.__pot = True
            self.__potion -= 1
            super().setHealth(super().getHealth() + 50)
        else:
            self.__pot = False

    def healName(self):
        if self.__pot:
            return "You drank a potion."
        return "You've run out of potions."

    #distinguishes between attacking and defending
    def doDamage(self, damage):
        if (self.__defense_mode):
            # Half Damage
            super().setHealth(super().getHealth() - (damage // 2))
        else:
            super().setHealth(super().getHealth() - damage)

    def resetHealth(self):
        super().setHealth(150)
        self.__potion = 6
        self.__fire = 10