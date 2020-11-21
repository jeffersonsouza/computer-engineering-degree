# Usando a biblioteca Pygame, escreva um programa que possui uma
# função que desenha um círculo verde de 100 px de diâmetro no
# centro da tela que se inicie o movimento da esquerda para a direita.
# Sempre que chegar em alguma extremidade, o círculo deve trocar a
# direção e aumentar a velocidade em 1. (código e printscreen)
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/TP3/

import pygame
from collections import namedtuple

# Coordinates
Position = namedtuple('Position', ['x', 'y'])

# Game init
pygame.init()
pygame.font.init()

screen_size = Position(x=800, y=600)
screen = pygame.display.set_mode(screen_size)
game_speed = 1
circle_radius = 50

# Colors
background = (232, 232, 232)
green = (100,133,75)

# Change title and logo
pygame.display.set_caption('Jefferson Souza dos Santos - TP3 - Item 13')

circle_position_x = screen.get_width() // 2 - circle_radius
circle_position_y = screen.get_height() // 2 - circle_radius
direction = 'right'

def draw_circle(position: Position):
    pygame.draw.circle(screen, green, position, circle_radius)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # paint the screen
    screen.fill(background)

    if circle_position_x >= screen.get_width() - circle_radius:
        game_speed += 1
        direction = 'left'
    elif circle_position_x <= circle_radius:
        game_speed += 1
        direction = 'right'

    circle_position_x += game_speed if direction == 'right' else -game_speed

    draw_circle(Position(x=circle_position_x, y=circle_position_y))

    # Update the display
    pygame.display.update()
    clock.tick(60)

pygame.display.quit()
