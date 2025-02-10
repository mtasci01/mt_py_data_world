import math
import pygame
pygame.init()

# 2 spinning circles forming a grid of lines

HEIGHT = 800
WIDTH = 600

window = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption('SPIN SPIN')
RED = (255,0,0)
BLUE = (0,0,255)
RADIUS_1 = 150
RADIUS_2 = 250
THICKNESS = 1

running = True
SPEED_1 = 0.05
SPEED_2 = 0.01
ORIGIN_X=350
ORIGIN_Y=300
t_1 = 0
t_2 = 0
lines = []
while running:
    window.fill([0,0,0])

    pos_1 = [ORIGIN_X + RADIUS_1*math.cos(t_1), ORIGIN_Y + RADIUS_1*math.sin(t_1)]
    pygame.draw.circle(window, RED, pos_1, 10)
    t_1 = t_1 + SPEED_1 

    pos_2 = [ORIGIN_X + RADIUS_2*math.cos(t_2), ORIGIN_Y + RADIUS_2*math.sin(t_2)]
    pygame.draw.circle(window, RED, pos_2, 10)
    t_2 = t_2 + SPEED_2

    lines.append([pos_1,pos_2])

    for line in lines:
        pygame.draw.line(window, BLUE, line[0],line[1],THICKNESS) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False     
    pygame.display.update()