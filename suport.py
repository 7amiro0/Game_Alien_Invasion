import pygame.image


class Support():
    def __init__(self, stats, ai_set, screen):
        self.screen = screen
        self.n = 1
        self.stats = stats
        self.ai_set = ai_set
        self.img = pygame.image.load("img/suport.bmp")
        self.ni = pygame.transform.scale(self.img, (50, 50))

        self.rect = self.ni.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom - 50
        self.posx = float(self.rect.centerx)
        self.posy = float(self.rect.centery)

    def update(self):
        if self.n == -1 and self.posx < self.screen_rect.right:
            self.posx += 4.5
        elif self.n == 1 and self.posx > self.screen_rect.left:
            self.posx -= 4.5
        elif self.screen_rect.left <= self.posx or self.screen_rect.right >= self.posx:
            self.n *= -1
        self.rect.centerx = self.posx

    def center(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.posx = float(self.rect.centerx)
        self.posy = float(self.rect.centery)

    def blit(self):
        self.screen.blit(self.ni, self.rect)
