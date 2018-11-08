from drawable import drawable
import pygame

class text(drawable):
    def __init__(self, x=0, y=0, text=""):
        super().__init__(x,y,180,40)
        self.__text = text

    def draw(self, s):
        if super().getVis():
            font = pygame.font.SysFont("comicsansms", super().getH())
            textS = font.render(self.__text, True, (255, 0, 255))
            r = self.get_rect()
            s.blit(textS, r)

    def get_rect(self):

        rect = pygame.Rect(super().getX(),super().getY(),super().getW(),super().getH())
        return rect

    def delete(self):
        super().setVis(False)

    def setY(self, y):
        super().setY(y)

    def setX(self, x):
        super().setX(x)