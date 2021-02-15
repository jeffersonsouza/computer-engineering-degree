# Usando o código anterior, escreva um novo programa que, quando as
# teclas ‘w’, ‘a’, ‘s’ e ‘d’ forem pressionadas, ele movimente o
# círculo com o texto “clique” nas direções corretas. Caso colida
# com algum retângulo, o retângulo que participou da colisão deve desaparecer.
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/AT/

import pygame, sys, random
from collections import namedtuple


class Game:
    # Coordinates
    Coordinate = namedtuple('Coordinate', ['x', 'y'])
    running = True
    background = (232, 232, 232)
    yellow = (255, 197, 1)
    red = (153, 5, 31)
    speed = 5

    squares = []

    def __init__(self):
        # Game init
        pygame.init()
        pygame.font.init()

        self.font = pygame.font.Font(None, 22)
        self.screenSize = self.Coordinate(x=800, y=600)
        self.screen = pygame.display.set_mode(self.screenSize)

        # Change title
        pygame.display.set_caption('Jefferson Souza dos Santos - AT - Questão 09')

        self.button = pygame.Rect(self.screen.get_width() // 2 - 50, 50, 100, 100)

        # main loop
        self.loop()

    def loop(self):
        # Game loop
        while self.running:
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.handle_quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse(event)
                if event.type == pygame.KEYDOWN:
                    self.handle_keys(event)

            # paint the screen
            self.screen.fill(self.background)

            self.draw_button('Clique')

            for square in self.squares:
                pygame.draw.rect(self.screen, self.yellow, square)

            # Update the display
            pygame.display.update()

        pygame.display.quit()

    def handle_quit(self):
        self.running = False
        sys.exit()

    def handle_mouse(self, event):
        if event.button == 1:
            position = pygame.mouse.get_pos()

            if self.button.collidepoint(position):
                rect = self.draw_square()
                self.squares.append(rect)
                self.collision_checker(rect)

    def handle_keys(self, event):
        if event.key == pygame.K_a:
            self.button.x -= self.speed

        if event.key == pygame.K_d:
            self.button.x += self.speed

        if event.key == pygame.K_w:
            self.button.y -= self.speed

        if event.key == pygame.K_s:
            self.button.y += self.speed

        for square in self.squares:
            if square.colliderect(self.button):
                self.squares.remove(square)

    def draw_button(self, text):
        pygame.draw.ellipse(self.screen, self.red, self.button)
        button_text = self.font.render(text, False, self.background)
        button_text_rect = button_text.get_rect(center=self.button.center)

        self.screen.blit(button_text, button_text_rect)

    def draw_square(self):
        x = random.randint(25, self.screen.get_width() - 25)
        y = random.randint(25, self.screen.get_height() - 25)

        return pygame.Rect(x, y, 60, 50)

    def collision_checker(self, rect):
        for square in self.squares:
            if square is not rect and square.colliderect(rect):
                self.squares.remove(square)
                if rect in self.squares:
                    self.squares.remove(rect)


game = Game()
