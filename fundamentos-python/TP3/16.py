# Usando a biblioteca Pygame, escreva um programa que desenha na tela
# estrelas de 5 pontas de tamanhos aleatórios a cada vez que o usuário
# clicar na tela. A ponta superior da estrela deve estar situada onde
# o usuário clicou. (código e printscreen)
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/TP3/

import math
import pygame
import random
from collections import namedtuple

# Coordinates
Position = namedtuple('Position', ['x', 'y'])

# Game init
pygame.init()
pygame.font.init()

screenSize = Position(x=800, y=600)
screen = pygame.display.set_mode(screenSize)

# Colors
background = (232, 232, 232)

# Change title and logo
pygame.display.set_caption('Jefferson Souza dos Santos - TP3 - Item 16')

# array to store stars points
stars = []

def get_star_points(sides, radius, position):
    points = []

    for n in range(sides * 2):
        rad = radius if n % 2 == 0 else radius // 2
        angle = (n * math.pi / sides) + (90 * math.pi / 60)

        point = (
            int(math.cos(angle) * rad + position[0]),
            int(math.sin(angle) * rad + position[1])
        )

        points.append(point)

    return points


# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_position = pygame.mouse.get_pos()

            # get star points and color
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            radius = random.randint(25, 150)
            stars.append((get_star_points(5, radius, [click_position[0], click_position[1] + radius]), color))

    # paint the screen
    screen.fill(background)

    for star in stars:
        pygame.draw.polygon(screen, star[1], star[0])

    # Update the display
    pygame.display.update()
    clock.tick(60)

pygame.display.quit()
