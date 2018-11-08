class Maze:
    #Inputs: Pointer to start room and exit room
    #Sets current to be start room
    def __init__(self,st=None,ex=None):
        #Room the player starts in
        self.__start_room = st
        #If the player finds this room they win
        self.__exit_room = ex
        #What room is the player currently in
        self.__current = st
    #Return the room the player is in (current)
    def getCurrent(self):
        return self.__current
    def moveNorth(self):
        if self.__current.getNorth() is not None:
            self.__current = self.__current.getNorth()
    def moveSouth(self):
        if self.__current.getSouth() is not None:
            self.__current = self.__current.getSouth()
    def moveEast(self):
        if self.__current.getEast() is not None:
            self.__current = self.__current.getEast()
    def moveWest(self):
        if self.__current.getWest() is not None:
            self.__current = self.__current.getWest()
    def atExit(self):
        if self.__current == self.__exit_room:
            return True
        else:
            return False
    def reset(self):
        self.__current = self.__start_room