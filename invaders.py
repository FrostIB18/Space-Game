import pygame

class Invader(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Invader, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/Invader_low.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Drawing invader on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Moving invaders"""
        self.y += 0.5
        self.rect.y = self.y