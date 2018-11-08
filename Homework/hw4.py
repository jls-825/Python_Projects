import pygame
from drawable import drawable
from text import text
from ball import ball
from block import block

#from the instructions
def intersect(rect1,rect2):
    if rect1.x < rect2.x + rect2.width and rect1.x + rect1.width > rect2.x and rect1.y < rect2.y + rect2.height and rect1.y + rect1.height > rect2.y:
        return True
    else:
        return False

#making game environment
pygame.init()
width = 500
height = 500
surface = pygame.display.set_mode((width, height))

ball = ball(20, 400)
score = text(0, 0, "Score: ")

bx1 = block(380, 380)
bx2 = block(400, 380)
bx3 = block(420, 380)
bx4 = block(440, 380)
bx5 = block(380, 360)
bx6 = block(400, 360)
bx7 = block(420, 360)
bx8 = block(440, 360)
bx9 = block(380, 340)
bx10 = block(400, 340)
bx11 = block(420, 340)
bx12 = block(440, 340)
bx13 = block(380, 320)
bx14 = block(400, 320)
bx15 = block(420, 320)
bx16 = block(440, 320)

box_list =[bx1, bx2, bx3, bx4, bx5, bx6, bx7, bx8, bx9, bx10, bx11, bx12, bx13, bx14, bx15, bx16]

#constants
g = 6.67
R = .7
eta = .5
dt = .1

#variables
x = 0
y = 0
xv = 0
yv = 0
scoreNum = 0

throw = False
box_clear = False

while (True):
    for event in pygame.event.get(): #exit
        if (event.type == pygame.QUIT) or \
            (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            xi, yi = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            xf, yf = pygame.mouse.get_pos()
            xv = (xf - xi)
            yv = -(yf - yi)
            throw = True

    if box_clear:
        box_reset = 0
        for bx in box_list:
            if bx.getVis() == False:
                box_reset += 1
                if box_reset == 16:
                    for bx in box_list:
                        bx.setVis(True)
            elif bx.getVis():
                pass
        box_clear = False

    pygame.draw.rect(surface, (255, 255, 255), [0, 0, 500, 500])
    pygame.draw.line(surface, (0, 0, 0), [0, 400], [500, 400])

    if throw:
        ball.setX(ball.getX() + (dt * xv))
        ball.setY(ball.getY() - (dt * yv))

        if ball.getY() >= 400:
            yv = -R * yv
            xv = eta * xv
        elif ball.getY() < 400:
            yv -= (g * dt)

        if ball.getX() <= -50 or ball.getX() >= 550:
            xv = 0
            yv = 0
            ball.setX(20)
            ball.setY(400)
            throw = False
            box_clear = True

        if (xv <= 0.1 and xv >= -0.1) and (yv <= 0.1 and yv >= -0.1):
            ball.setX(20)
            ball.setY(400)
            throw = False
            box_clear = True

    for box in box_list:
        box.draw(surface)
        collision = intersect(ball.get_rect(), box.get_rect())
        vis = box
        if collision:
            if vis.getVis():
                scoreNum += 1
                vis.setVis(False)
            elif vis.getVis() == False:
                pass
        else:
            pass

        box_clear += 1
    num = text(150, 0, str(scoreNum))
    ball.draw(surface)
    score.draw(surface)
    num.draw(surface)
    pygame.display.update()




