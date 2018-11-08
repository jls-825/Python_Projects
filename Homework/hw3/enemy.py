import abc

#abstract base class
class enemy(metaclass=abc.ABCMeta):
    def __init__(self, n, h):
        self.__name = n
        self.__health = h
        return

    def __str__(self):
        return self.__name + ":" + self.__health + " health"

    def getName(self):
        return self.__name

    @abc.abstractmethod
    def getDescription(self):
        pass

    @abc.abstractmethod
    def basicAttack(self, enemy):
        pass

    # Print the name of the attack used
    @abc.abstractmethod
    def basicName(self):
        pass

    # Defense Move
    @abc.abstractmethod
    def defenseAttack(self, enemy):
        pass

    # Print out the name of the attack used
    @abc.abstractmethod
    def defenseName(self):
        pass

    # Special Attack
    @abc.abstractmethod
    def specialAttack(self, enemy):
        pass

    @abc.abstractmethod
    def specialName(self):
        pass

    # Health Management
    def getHealth(self):
        return self.__health

    def setHealth(self,x):
        self.__health = x


    @abc.abstractmethod
    def doDamage(self, damage):
        pass