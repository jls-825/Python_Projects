class Birthday():
    def __init__(self, d, m , y):
        self.__day = d
        self.__month = m
        self.__year = y
    def __str__(self):
        return '%d/%d/%d' % (self.__day, self.__month, self.__year)

    def __hash__(self):
        return (int(self.__day) + int(self.__month) + int(self.__year)) % 12

    def __eq__(self, other):
        if self.__year != other.__year or self.__month != other.__month or self.__day != other.__day:
            return False
        else:
            return True


if __name__ == '__main__':
    James = Birthday(2, 21, 1999)
    K = Birthday(1, 31, 2001)
    Polk = Birthday(2,21,1999)
    print(James)


