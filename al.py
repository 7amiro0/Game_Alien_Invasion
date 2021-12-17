from pygame.sprite import Sprite 
import pygame


class Alien(Sprite):
    def __init__(self, ai_set, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_set = ai_set

        self.image = pygame.image.load("img/al.bmp")
        self.ni = pygame.transform.scale(self.image, (120, 100))
        self.rect = self.ni.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.ni, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.ai_set.alien_speed_factor * self.ai_set.fleet_direction)
        self.rect.x = self.x
