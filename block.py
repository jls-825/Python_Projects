from drawable import drawable
import pygame

class block(drawable):
    def __init__(self, x, y):
        super().__init__(x,y,20,20)

    def draw(self, s):
        if super().getVis():
            pygame.draw.rect(s,(0,0,255),(super().getX(),super().getY(),super().getW(),super().getH()))
            pygame.draw.rect(s,(0,0,0),(super().getX(),super().getY(),super().getW(),super().getH()),1)

    def get_rect(self):
        rect = pygame.Rect((super().getX()),(super().getY()),(super().getW()),(super().getH()))
        return rect

    def delete(self):
        super().setVis(False)

    def setY(self, y):
        super().setY(y)

    def setX(self, x):
        super().setX(x)