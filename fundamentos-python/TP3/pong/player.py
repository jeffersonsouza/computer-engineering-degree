import pygame

class Player:
    name = ''
    score = 0
    kind = ''
    speed = 0

    position_x = 0
    position_y = 0
    width = 10
    height = 150
    position_change_y = 0

    rect = None

    def __init__(self, x=0, y=0, kind='human', width=10, height=150):
        self.position_x = x
        self.position_y = y
        self.kind = kind
        self.width = width
        self.height = height

        self.rect = pygame.Rect(self.position_x, self.position_y, self.width, self.height)

    def draw(self):
        # self.rect = pygame.Rect(self.position_x, self.position_y, self.width, self.height)

        return self.rect

    def add_point(self, points=1):
        self.score += points

        if self.score % 10 == 0 and self.kind == 'human':
            self.ten_point_sound()

    def ten_point_sound(self):
        point = pygame.mixer.Sound("coin6.wav")
        pygame.mixer.Sound.play(point)
        pygame.mixer.music.stop()
