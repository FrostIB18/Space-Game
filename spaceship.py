import pygame
from pygame.sprite import Sprite

class Spaceship(Sprite):

    def __init__(self, screen):
        super(Spaceship, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/spaceship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """Drawing spaceship"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update of spaceship position"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 16
        elif self.mleft and self.rect.left > 0:
            self.center -= 16

        self.rect.centerx = self.center

    def create_spaceship(self):
        """Creating a spaceship again"""
        self.center = self.screen_rect.centerx

class Spaceship_live(Spaceship):

    def __init__(self, screen):
        super(Spaceship_live, self).__init__(screen)
        self.image = pygame.image.load("images/spaceship_live.png")