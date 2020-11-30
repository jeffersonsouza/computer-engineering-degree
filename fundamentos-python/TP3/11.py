# Usando a biblioteca Pygame, escreva um programa que possui uma função que
# desenha um círculo azul de 100 px de diâmetro no centro da tela que se
# move da esquerda para a direita. Sempre que chegar na extremidade direita,
# o círculo deve voltar à extremidade esquerda, retomando o movimento da
# esquerda para a direita. (código e printscreen)
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

# Colors
background = (232, 232, 232)
blue = (41,59,136)

# Change title and logo
pygame.display.set_caption('Jefferson Souza dos Santos - TP3 - Item 11')

circle_position_x = screen.get_width() // 2 - 50
circle_position_y = screen.get_height() // 2 - 50
direction = 'right'

def draw_circle(position: Position):
    pygame.draw.circle(screen, blue, position, 50)

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

    if circle_position_x == screen.get_width() - 50:
        direction = 'left'
    elif circle_position_x == 50:
        direction = 'right'


    circle_position_x += game_speed if direction == 'right' else -game_speed

    draw_circle(Position(x=circle_position_x, y=circle_position_y))

    # Update the display
    pygame.display.update()
    clock.tick(120)

pygame.display.quit()
