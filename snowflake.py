import drawable
import pygame

class snowflake(drawable):
    def __init__(self):
        super().__init__(x, 0)
        self.__x = x
        self.__y = 0
        #self.__line1 = (self.__x + 5, self.__y)
        #self.__line2 = (self.__x, self.__y + 5)
        #self.__line3 = (self.__x + 5, self.__y + 5)
        #self.__line4 = (self.__x + 5, self.__y - 5)

    def draw(self, surface):
        pygame.draw.line(surface, (255, 255, 255), self.__x + 5, self.__y, 1)
        pygame.draw.line(surface, (255, 255, 255), self.__x, self.__y + 5, 1)
        pygame.draw.line(surface, (255, 255, 255), self.__x + 5, self.__y + 5, 1)
        pygame.draw.line(surface, (255, 255, 255), self.__x + 5, self.__y - 5, 1)
