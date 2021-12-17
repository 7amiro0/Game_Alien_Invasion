import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_set, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_set = ai_set
        self.img = pygame.image.load('img/sp.bmp')
        self.image = pygame.transform.scale(self.img, (80, 100))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom - 50
        self.cx = float(self.rect.centerx)
        self.cy = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.cx += 4.5
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.cx -= 4.5
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.cy -= 4.5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.cy += 4.5
        self.rect.centerx = self.cx
        self.rect.centery = self.cy

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.cx = float(self.rect.centerx)
        self.cy = float(self.rect.centery)

    def blite(self):
        self.screen.blit(self.image, self.rect)
