import pygame


class Ball:
    position_x = 0
    position_y = 0
    position_change_x = 1
    position_change_y = 1
    width = 25
    height = 25

    point_value = 1

    speed = 1

    rect = None

    def __init__(self, x=0, y=0, width=25, height=25):
        self.position_x = x
        self.position_y = y
        self.width = width
        self.height = height

        self.rect = pygame.Rect(self.position_x, self.position_y, self.width, self.height)

    def draw(self):
        self.rect = pygame.Rect(self.position_x, self.position_y, self.width, self.height)

        return self.rect

    def ball_sound(self):
        hit = pygame.mixer.Sound("jumpland.wav")
        pygame.mixer.Sound.play(hit)
        pygame.mixer.music.stop()

    def fail_sound(self):
        fail = pygame.mixer.Sound("fail.wav")
        pygame.mixer.Sound.play(fail)
        pygame.mixer.music.stop()

    def success_sound(self):
        point = pygame.mixer.Sound("success.wav")
        pygame.mixer.Sound.play(point)
        pygame.mixer.music.stop()
