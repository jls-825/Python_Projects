#Jeanna Shellenberger Section 068

class socialite:
    #initializing
    def __init__(self):
        self.__LastN = ''
        self.__FirstN = ''
        self.__pic = ''
        self.__web = ''
        self.__des = ''
        self.__UserID = ''

    #string method
    def str(self):
        str = 'Name: ' + self.__FirstN + ' ' + self.__LastN + '\nUser ID: ' + self.__UserID + '\nPicture: ' + self.__pic + '\nWebsite: ' + self.__web + '\nWebsite Description: ' + self.__des
        return str

    #mutator methods
    def setLastName(self, l):
        self.__LastN = l

    def setFirstName(self, f):
        self.__FirstN = f

    def setUserID(self, n):
        self.__UserID = n

    def setPicture(self, p):
        self.__pic = p

    def setWebsite(self, w):
        self.__web = w

    def setDescription(self, d):
        self.__des = d

    #accessor methods
    def getLastName(self):
        return self.__LastN

    def getFirstName(self):
        return self.__FirstN

    def getPicture(self):
        return self.__pic

    def getWebsite(self):
        return self.__web

    def getDescription(self):
        return self.__des

    def getUserID(self):
        return self.__UserID
