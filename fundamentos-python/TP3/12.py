# Usando a biblioteca Pygame, escreva um programa que possui uma função
# que desenha um círculo amarelo de 100 px de diâmetro no centro da tela
# que se move sempre em velocidade permanente na direção que o usuário
# indicar através das teclas. Similar ao item anterior, sempre que chegar
# em uma extremidade, o círculo deve voltar à extremidade oposta e continuar
# o com a última direção que o usuário indicou. (código e printscreen)
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
game_speed = 2
circle_radius = 50

# Colors
background = (232, 232, 232)
yellow = (255, 197, 1)

# Change title and logo
pygame.display.set_caption('Jefferson Souza dos Santos - TP3 - Item 12')

circle_position_x = screen.get_width() // 2 - circle_radius
circle_position_y = screen.get_height() // 2 - circle_radius
direction = 'right'

def draw_circle(position: Position):
    pygame.draw.circle(screen, yellow, position, circle_radius)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                direction = 'left'

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                direction = 'right'

    # paint the screen
    screen.fill(background)

    if circle_position_x == screen.get_width() - circle_radius:
        direction = 'left'
    elif circle_position_x == circle_radius:
        direction = 'right'

    circle_position_x += game_speed if direction == 'right' else -game_speed

    draw_circle(Position(x=circle_position_x, y=circle_position_y))

    # Update the display
    pygame.display.update()
    clock.tick(120)

pygame.display.quit()
