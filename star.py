import pygame
from random import randint
from pygame.sprite import Sprite 


class Star(Sprite):
    def __init__(self, ai_set, screen):
        super(Star, self).__init__()
        self.screen = screen
        self.ai_set = ai_set
        self.size = randint(0, 80)

        self.image = pygame.image.load("img/star1.bmp")
        self.ni = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.ni.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.screen_rect.left + randint(ai_set.wi - ai_set.wi, ai_set.wi)
        self.rect.y = self.screen_rect.top + randint(ai_set.he - ai_set.he, ai_set.he)

    def blite(self):
        self.screen.blit(self.ni, self.rect)
