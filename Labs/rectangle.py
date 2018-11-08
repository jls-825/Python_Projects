import pygame
import drawable
pygame.init()

class rectangle(drawable):
    def __init__(self, w, h, c):
        super().__init__(x, y)
        self.__x = x
        self.__y = y
        self.__width = w
        self.__height = h
        self.__color = c

    def draw(self, surface):
        pygame.draw.polygon(surface, self.__color, (self.__x, self.__y), self.__width)
