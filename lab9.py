import pygame
pygame.init()
width = 1000
height = 600
surface = pygame.display.set_mode((width, height))

while (True):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
        pygame.display.update()
        surface.fill((0, 100, 200))
        pygame.draw.polygon(surface, (50, 205, 50), [(0, 450), (1000, 450), (1000, 600), (0, 600)])

        if isinstance(imgSurface, snowflake):
            pygame.blit