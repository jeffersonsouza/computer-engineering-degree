# usados sons obtidos em https://freesound.org/ sob a licença creative commons
import pygame, sys, random
from player import Player
from ball import Ball
from collections import namedtuple

# Game init
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 32)
font_name = 'Eight-Bit Madness.ttf'

# Coordinates
Coordinate = namedtuple('Coordinate', ['x', 'y'])

screenSize = Coordinate(x=800, y=600)
screen = pygame.display.set_mode(screenSize)

# Change title and logo
pygame.display.set_caption('Jefferson Souza dos Santos - TP 3 - Pong')

# Colors
background = (232, 232, 232)
grey = (100, 100, 100)
red = (153, 5, 31)

# Players and Ball
player = Player(10, screen.get_height() // 2 - 75)
com = Player(screen.get_width() - 20, screen.get_height() // 2 - 75, 'com')
ball = Ball(screen.get_width() // 2 - 12, screen.get_height() // 2 - 12)


def draw_ball():
    if ball.rect.top <= 0 or ball.rect.bottom >= screen.get_height():
        ball.position_change_y *= -1

    if ball.rect.left <= 0 or ball.rect.right >= screen.get_width():
        ball.position_change_x *= -1

    if ball.rect.colliderect(player) or ball.rect.colliderect(com):
        ball.ball_sound()
        ball.position_change_x *= -1

    if ball.rect.colliderect(player):
        player.add_point(ball.point_value)

        if player.score % 10 == 0:
            ball.speed += 1
        if player.score % 20 == 0:
            ball.point_value += 1

    if ball.rect.colliderect(com):
        com.add_point(ball.point_value)

    ball.position_x += ball.position_change_x * ball.speed
    ball.position_y += ball.position_change_y * ball.speed

    if ball.rect.left <= 0:
        ball.fail_sound()
        reset()
    if ball.rect.right >= screen.get_width():
        ball.success_sound()
        reset()

    ball.draw()

    pygame.draw.ellipse(screen, grey, ball.rect)


def reset():
    ball.position_x = screen.get_width() // 2
    ball.position_y = screen.get_height() // 2
    ball.position_change_x *= random.choice((-1, 1))
    ball.position_change_y *= random.choice((-1, 1))
    ball.speed = 1

    player.score = 0
    com.score = 0


def draw_player():
    player.rect.y += player.speed

    if player.rect.top <= 0:
        player.rect.top = 0
    if player.rect.bottom >= screen.get_height():
        player.rect.bottom = screen.get_height()

    pygame.draw.rect(screen, grey, player.rect)

    font = pygame.font.Font(font_name, 22)
    text = font.render(f"Player: {player.score}", True, (0, 0, 0))
    position = text.get_rect(center=(70, 20))
    screen.blit(text, position)


def draw_com():
    pygame.draw.rect(screen, grey, com.rect)

    if com.rect.top < ball.rect.top:
        com.rect.y += ball.speed
    if com.rect.bottom > ball.rect.bottom:
        com.rect.y -= ball.speed

    font = pygame.font.Font(font_name, 22)
    text = font.render(f"COM: {com.score}", True, (0, 0, 0))
    position = text.get_rect(center=(screen.get_width() - 100, 20))
    screen.blit(text, position)


def draw_level():
    font = pygame.font.Font(font_name, 22)
    text = font.render(f"Level: {ball.speed}", True, (0, 0, 0))
    position = text.get_rect(center=(65, 40))
    screen.blit(text, position)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.speed -= ball.speed
                player.draw()

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.speed += ball.speed
                player.draw()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.speed += ball.speed
                player.draw()

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.speed -= ball.speed
                player.draw()

    # paint the screen
    screen.fill(background)

    pygame.draw.aaline(screen, grey, (screen.get_width() // 2, 0), (screen.get_width() // 2, screen.get_height()))

    draw_ball()
    draw_player()
    draw_com()
    draw_level()

    # Update the display
    pygame.display.update()

    # Set FPS rate
    clock.tick(150)

pygame.display.quit()
