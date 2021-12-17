import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    toogle = False

    def __init__(self, ai_seting, screen, ship):
        super(Bullet, self).__init__()

        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 50)

        self.rect.midtop = ship.rect.midtop
        self.y = float(self.rect.y) + 50
        self.rect.x += 30 if Bullet.toogle else -30
        Bullet.toogle = not Bullet.toogle

        self.color = 255, 0, 0

        self.speed_b = 10

    def update(self):
        self.y -= self.speed_b
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
