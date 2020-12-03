# Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela
# em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta),
# toda vez que a tecla espaço for pressionada ou o botão direito for clicado.
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

    squares = []

    def __init__(self):
        # Game init
        pygame.init()

        self.screenSize = self.Coordinate(x=800, y=600)
        self.screen = pygame.display.set_mode(self.screenSize)

        # Change title
        pygame.display.set_caption('Jefferson Souza dos Santos - AT - Questão 07')

        # main loop
        self.loop()

    def loop(self):
        # Game loop
        while self.running:
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.handle_quit()
                if event.type == pygame.KEYDOWN:
                    self.handle_key_down(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse(event)

            # paint the screen
            self.screen.fill(self.background)

            for square in self.squares:
                pygame.draw.rect(self.screen, self.yellow, square)

            # Update the display
            pygame.display.update()

        pygame.display.quit()

    def handle_quit(self):
        self.running = False
        sys.exit()

    def handle_key_down(self, event):
        if event.key == pygame.K_SPACE:
            self.squares.append(self.draw_square())

    def handle_mouse(self, event):
        if event.button == 3:
            self.squares.append(self.draw_square())

    def draw_square(self):
        x = random.randint(25, self.screen.get_width() - 25)
        y = random.randint(25, self.screen.get_height() - 25)

        return pygame.Rect(x, y, 50, 50)


game = Game()
