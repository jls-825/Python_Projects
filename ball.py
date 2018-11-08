import pygame
from drawable import drawable

class ball(drawable):
    def __init__(self, x=0, y=0):
        super().__init__(x,y,16,16)

    def draw(self, s):
        if super().getVis():
            pygame.draw.circle(s,(255,0,0),(int(super().getX()),int(super().getY())),int(super().getW()//2))

    def get_rect(self):
        rect = pygame.Rect((int(super().getX())),(int(super().getY())),(super().getW()),(super().getH()))
        return rect

    def delete(self):
        super().setVis(False)

    def setY(self, y):
        super().setY(y)
    def setX(self, x):
        super().setX(x)