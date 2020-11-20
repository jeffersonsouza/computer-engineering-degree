# Usando a biblioteca Pygame, escreva um programa que possui uma função que
# desenha um círculo azul de 100 px de diâmetro no centro da tela. (código e printscreen)
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/TP3/

import pygame
from collections import namedtuple

# Coordinates
Position = namedtuple('Position', ['x', 'y'])

# Game init
pygame.init()
pygame.font.init()

screenSize = Position(x=800, y=600)
screen = pygame.display.set_mode(screenSize)

# Colors
background = (232,232,232)
blue = (41,59,136)

# Change title and logo
pygame.display.set_caption('Jefferson Souza dos Santos - TP3 - Item 09')

def draw_circle():
    pygame.draw.circle(screen, blue, (screen.get_width() // 2, screen.get_height() // 2), 50)

# Game loop
running = True
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # paint the screen
    screen.fill(background)

    draw_circle()

    # Update the display
    pygame.display.update()

pygame.display.quit()
